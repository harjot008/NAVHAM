from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
import sqlite3
import hashlib
import os
from datetime import datetime
from functools import wraps
import random

app = Flask(__name__)
app.secret_key = 'navham-pm-internship-scheme-2025-secret-key'  # Change in production

# Database configuration
DATABASE = 'internships.db'

def get_db_connection():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database with schema"""
    with open('models/schema.sql', 'r') as f:
        schema = f.read()
    
    conn = get_db_connection()
    conn.executescript(schema)
    conn.commit()
    conn.close()

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    """Verify password against hash"""
    return hashlib.sha256(password.encode()).hexdigest() == hashed_password

def login_required(f):
    """Decorator to require login for certain routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def get_user_candidate_info(user_id):
    """Get user and candidate information"""
    conn = get_db_connection()
    
    user = conn.execute(
        'SELECT * FROM users WHERE id = ?', (user_id,)
    ).fetchone()
    
    candidate = conn.execute(
        'SELECT * FROM candidates WHERE user_id = ?', (user_id,)
    ).fetchone()
    
    conn.close()
    return user, candidate

def get_recommended_internships(candidate_id, limit=5):
    """Get recommended internships based on candidate profile"""
    conn = get_db_connection()
    
    # Get candidate info
    candidate = conn.execute(
        'SELECT * FROM candidates WHERE candidate_id = ?', (candidate_id,)
    ).fetchone()
    
    if not candidate:
        conn.close()
        return []
    
    # Simple recommendation logic based on location and skills
    query = '''
        SELECT *, 
               CASE 
                   WHEN location_state = ? THEN 3
                   WHEN location_city = ? THEN 2
                   ELSE 1
               END as location_score,
               CASE 
                   WHEN skills_required LIKE ? THEN 3
                   WHEN skills_required IS NULL OR skills_required = '' THEN 1
                   ELSE 0
               END as skills_score
        FROM internships 
        ORDER BY (location_score + skills_score) DESC, stipend DESC
        LIMIT ?
    '''
    
    # Create skill pattern for matching
    skills = candidate['skills'] or ''
    skill_pattern = f'%{skills.split(",")[0].strip()}%' if skills else '%%'
    
    internships = conn.execute(query, (
        candidate['state'], 
        candidate['city'], 
        skill_pattern, 
        limit
    )).fetchall()
    
    conn.close()
    return internships

@app.route('/')
def index():
    """Home page with login/register form"""
    if 'user_id' in session:
        # Check if user has completed profile
        user, candidate = get_user_candidate_info(session['user_id'])
        if candidate:
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('complete_profile_form'))
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    """Handle user registration"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        name = data.get('name', '')
        
        if not email or not password:
            return jsonify({
                'success': False, 
                'message': 'Email and password are required'
            }), 400
        
        # Check if user already exists
        conn = get_db_connection()
        existing_user = conn.execute(
            'SELECT id FROM users WHERE email = ?', (email,)
        ).fetchone()
        
        if existing_user:
            conn.close()
            return jsonify({
                'success': False, 
                'message': 'Email already registered'
            }), 400
        
        # Create new user
        password_hash = hash_password(password)
        cursor = conn.execute(
            'INSERT INTO users (email, password_hash) VALUES (?, ?)',
            (email, password_hash)
        )
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        # Set session
        session['user_id'] = user_id
        session['email'] = email
        
        return jsonify({
            'success': True, 
            'message': 'Registration successful',
            'redirect': url_for('complete_profile_form')
        })
        
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': 'Registration failed. Please try again.'
        }), 500

@app.route('/login', methods=['POST'])
def login():
    """Handle user login"""
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({
                'success': False, 
                'message': 'Email and password are required'
            }), 400
        
        # Check user credentials
        conn = get_db_connection()
        user = conn.execute(
            'SELECT id, email, password_hash FROM users WHERE email = ?', 
            (email,)
        ).fetchone()
        conn.close()
        
        if not user or not verify_password(password, user['password_hash']):
            return jsonify({
                'success': False, 
                'message': 'Invalid email or password'
            }), 401
        
        # Set session
        session['user_id'] = user['id']
        session['email'] = user['email']
        
        # Check if profile is complete
        user, candidate = get_user_candidate_info(user['id'])
        redirect_url = url_for('dashboard') if candidate else url_for('complete_profile_form')
        
        return jsonify({
            'success': True, 
            'message': 'Login successful',
            'redirect': redirect_url
        })
        
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': 'Login failed. Please try again.'
        }), 500

@app.route('/logout')
def logout():
    """Handle user logout"""
    session.clear()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('index'))

@app.route('/complete-profile')
@login_required
def complete_profile_form():
    """Show profile completion form"""
    user, candidate = get_user_candidate_info(session['user_id'])
    return render_template('complete_profile.html', user=user, candidate=candidate)

@app.route('/submit-profile', methods=['POST'])
@login_required
def submit_profile():
    """Handle profile form submission"""
    try:
        data = request.get_json() if request.is_json else request.form
        
        required_fields = ['name', 'age', 'gender', 'city', 'state', 'education']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'success': False, 
                    'message': f'{field.title()} is required'
                }), 400
        
        name = data.get('name')
        age = int(data.get('age'))
        gender = data.get('gender')
        city = data.get('city')
        state = data.get('state')
        education = data.get('education')
        skills = data.get('skills', '')
        interests = data.get('interests', '')
        
        conn = get_db_connection()
        
        # Check if candidate profile already exists
        existing_candidate = conn.execute(
            'SELECT candidate_id FROM candidates WHERE user_id = ?', 
            (session['user_id'],)
        ).fetchone()
        
        if existing_candidate:
            # Update existing profile
            conn.execute(
                '''UPDATE candidates 
                   SET name=?, age=?, gender=?, city=?, state=?, education=?, skills=?
                   WHERE user_id=?''',
                (name, age, gender, city, state, education, skills, session['user_id'])
            )
        else:
            # Create new candidate profile
            cursor = conn.execute(
                '''INSERT INTO candidates 
                   (user_id, name, age, gender, city, state, education, skills)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (session['user_id'], name, age, gender, city, state, education, skills)
            )
            session['candidate_id'] = cursor.lastrowid
        
        conn.commit()
        conn.close()
        
        session['profile_complete'] = True
        
        if request.is_json:
            return jsonify({
                'success': True, 
                'message': 'Profile completed successfully',
                'redirect': url_for('dashboard')
            })
        else:
            flash('Profile completed successfully!', 'success')
            return redirect(url_for('dashboard'))
        
    except Exception as e:
        if request.is_json:
            return jsonify({
                'success': False, 
                'message': 'Failed to complete profile. Please try again.'
            }), 500
        else:
            flash('Failed to complete profile. Please try again.', 'error')
            return redirect(url_for('complete_profile_form'))

@app.route('/dashboard')
@login_required
def dashboard():
    """Main dashboard page"""
    user, candidate = get_user_candidate_info(session['user_id'])
    
    if not candidate:
        return redirect(url_for('complete_profile_form'))
    
    # Get recommended internships
    recommended_internships = get_recommended_internships(candidate['candidate_id'])
    
    return render_template('dashboard.html', 
                         user=user, 
                         candidate=candidate, 
                         internships=recommended_internships)

@app.route('/edit-profile')
@login_required
def edit_profile():
    """Edit profile page"""
    user, candidate = get_user_candidate_info(session['user_id'])
    return render_template('edit_profile.html', user=user, candidate=candidate)

@app.route('/internships')
@login_required
def internships():
    """Show all internships page"""
    user, candidate = get_user_candidate_info(session['user_id'])
    
    if not candidate:
        return redirect(url_for('complete_profile_form'))
    
    # Get all internships with filtering options
    conn = get_db_connection()
    
    # Get filter parameters
    state_filter = request.args.get('state', '')
    sector_filter = request.args.get('sector', '')
    
    query = 'SELECT * FROM internships WHERE 1=1'
    params = []
    
    if state_filter:
        query += ' AND location_state LIKE ?'
        params.append(f'%{state_filter}%')
    
    if sector_filter:
        query += ' AND sector LIKE ?'
        params.append(f'%{sector_filter}%')
    
    query += ' ORDER BY stipend DESC'
    
    all_internships = conn.execute(query, params).fetchall()
    
    # Get unique states and sectors for filter dropdowns
    states = conn.execute('SELECT DISTINCT location_state FROM internships WHERE location_state IS NOT NULL').fetchall()
    sectors = conn.execute('SELECT DISTINCT sector FROM internships WHERE sector IS NOT NULL').fetchall()
    
    conn.close()
    
    return render_template('internships.html', 
                         user=user, 
                         candidate=candidate, 
                         internships=all_internships,
                         states=states,
                         sectors=sectors,
                         current_state=state_filter,
                         current_sector=sector_filter)

@app.route('/apply-internship', methods=['POST'])
@login_required
def apply_internship():
    """Apply for an internship"""
    try:
        data = request.get_json()
        internship_id = data.get('internship_id')
        
        user, candidate = get_user_candidate_info(session['user_id'])
        if not candidate:
            return jsonify({
                'success': False,
                'message': 'Please complete your profile first'
            }), 400
        
        conn = get_db_connection()
        
        # Check if already applied
        existing_application = conn.execute(
            'SELECT * FROM applications WHERE candidate_id = ? AND internship_id = ?',
            (candidate['candidate_id'], internship_id)
        ).fetchone()
        
        if existing_application:
            conn.close()
            return jsonify({
                'success': False,
                'message': 'You have already applied for this internship'
            }), 400
        
        # Create application
        conn.execute(
            'INSERT INTO applications (candidate_id, internship_id, status) VALUES (?, ?, ?)',
            (candidate['candidate_id'], internship_id, 'Applied')
        )
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True,
            'message': 'Application submitted successfully!'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Failed to submit application. Please try again.'
        }), 500

@app.route('/help-support')
@login_required
def help_support():
    """Help and support page"""
    user, candidate = get_user_candidate_info(session['user_id'])
    return render_template('help_support.html', user=user, candidate=candidate)

@app.route('/api/user-status')
def user_status():
    """Check if user is logged in"""
    if 'user_id' in session:
        user, candidate = get_user_candidate_info(session['user_id'])
        return jsonify({
            'logged_in': True,
            'user_id': session['user_id'],
            'email': session['email'],
            'profile_complete': candidate is not None
        })
    else:
        return jsonify({'logged_in': False})

if __name__ == '__main__':
    # Initialize database on first run
    if not os.path.exists(DATABASE):
        init_db()
    
    app.run(debug=True, host='0.0.0.0', port=5000)