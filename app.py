from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import sqlite3
import hashlib
import os
from datetime import datetime
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'  # Change this in production

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

@app.route('/')
def index():
    """Home page with login/register form"""
    if 'user_id' in session:
        # User is already logged in, redirect to dashboard or profile
        return redirect(url_for('profile'))
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
            'redirect': url_for('profile')
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
        
        return jsonify({
            'success': True, 
            'message': 'Login successful',
            'redirect': url_for('profile')
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
    return redirect(url_for('index'))

@app.route('/profile')
@login_required
def profile():
    """User profile page (placeholder for now)"""
    conn = get_db_connection()
    
    # Get user info
    user = conn.execute(
        'SELECT * FROM users WHERE id = ?', 
        (session['user_id'],)
    ).fetchone()
    
    # Check if candidate profile exists
    candidate = conn.execute(
        'SELECT * FROM candidates WHERE user_id = ?', 
        (session['user_id'],)
    ).fetchone()
    
    conn.close()
    
    return render_template('profile.html', user=user, candidate=candidate)

@app.route('/complete-profile', methods=['POST'])
@login_required
def complete_profile():
    """Handle candidate profile completion"""
    try:
        data = request.get_json()
        name = data.get('name')
        age = data.get('age')
        gender = data.get('gender')
        city = data.get('city')
        state = data.get('state')
        education = data.get('education')
        skills = data.get('skills')
        
        if not all([name, age, gender, city, state, education]):
            return jsonify({
                'success': False, 
                'message': 'All fields are required'
            }), 400
        
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
            conn.execute(
                '''INSERT INTO candidates 
                   (user_id, name, age, gender, city, state, education, skills)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (session['user_id'], name, age, gender, city, state, education, skills)
            )
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'success': True, 
            'message': 'Profile updated successfully'
        })
        
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': 'Failed to update profile. Please try again.'
        }), 500

@app.route('/api/user-status')
def user_status():
    """Check if user is logged in"""
    if 'user_id' in session:
        return jsonify({
            'logged_in': True,
            'user_id': session['user_id'],
            'email': session['email']
        })
    else:
        return jsonify({'logged_in': False})

if __name__ == '__main__':
    # Initialize database on first run
    if not os.path.exists(DATABASE):
        init_db()
    
    app.run(debug=True, host='0.0.0.0', port=5000)