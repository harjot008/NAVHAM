# NAVHAM - User Authentication System Setup

This document provides instructions for setting up and running the Flask-based user authentication system for the PM Internship Scheme recommendation engine.

## Features Implemented

- User registration and login system
- Secure password hashing using SHA-256
- Session management
- User profile creation and updating
- Integration with existing SQLite database schema
- Mobile-responsive design
- Real-time form validation

## Prerequisites

- Python 3.7 or higher
- Flask and dependencies (see requirements.txt)

## Installation Steps

### 1. Clone and Setup

```bash
# Navigate to your project directory
cd NAVHAM

# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Setup

The application will automatically initialize the database on first run using the schema in `models/schema.sql`. The database file `internships.db` should already exist in your project.

### 3. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## File Structure

```
NAVHAM/
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── internships.db            # SQLite database
├── models/
│   └── schema.sql            # Database schema
├── static/
│   ├── css/
│   │   └── home.css          # Existing styles
│   └── js/
│       └── auth.js           # Authentication JavaScript
├── templates/
│   ├── index.html            # Login/Register page
│   └── profile.html          # User profile page
└── SETUP_INSTRUCTIONS.md     # This file
```

## API Endpoints

### Authentication
- `GET /` - Home page with login/register form
- `POST /login` - User login (JSON)
- `POST /register` - User registration (JSON)
- `GET /logout` - User logout

### User Management
- `GET /profile` - User profile page (requires login)
- `POST /complete-profile` - Complete/update user profile (JSON)
- `GET /api/user-status` - Check login status (JSON)

## Request/Response Examples

### Registration
```json
// POST /register
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword"
}

// Response
{
    "success": true,
    "message": "Registration successful",
    "redirect": "/profile"
}
```

### Login
```json
// POST /login
{
    "email": "john@example.com",
    "password": "securepassword"
}

// Response
{
    "success": true,
    "message": "Login successful",
    "redirect": "/profile"
}
```

### Complete Profile
```json
// POST /complete-profile
{
    "name": "John Doe",
    "age": 22,
    "gender": "Male",
    "city": "Mumbai",
    "state": "Maharashtra",
    "education": "Bachelor's",
    "skills": "Python, Data Analysis, Communication"
}

// Response
{
    "success": true,
    "message": "Profile updated successfully"
}
```

## Database Schema

The system uses the existing database schema with these main tables:

- `users` - Authentication data (id, email, password_hash, created_at)
- `candidates` - User profile data (candidate_id, user_id, name, age, gender, city, state, education, skills)

## Security Features

1. **Password Hashing**: Uses SHA-256 for password security
2. **Session Management**: Flask sessions for user state
3. **Input Validation**: Both client and server-side validation
4. **SQL Injection Prevention**: Parameterized queries
5. **XSS Prevention**: Proper input sanitization

## Testing the System

1. **Registration**: Go to `http://localhost:5000`, click "Sign Up", and create a new account
2. **Login**: Use the created credentials to log in
3. **Profile**: Complete your profile with required information
4. **Logout**: Use the logout button to end your session

## Troubleshooting

### Common Issues

1. **Database not found**: Make sure `internships.db` exists in the project root
2. **CSS not loading**: Check that `static/css/home.css` exists
3. **JavaScript errors**: Check browser console for detailed errors
4. **Session issues**: Clear browser cookies and restart the application

### Development Mode

The application runs in debug mode by default. For production:

1. Change `app.secret_key` to a secure random string
2. Set `debug=False` in `app.run()`
3. Use a production WSGI server like Gunicorn

## Next Steps

After implementing user authentication, the next phases would be:

1. **Recommendation Engine**: Build the AI-based internship recommendation system
2. **Internship Management**: Display and filter available internships
3. **Application System**: Allow users to apply for internships
4. **Dashboard**: Create a comprehensive user dashboard
5. **Mobile Optimization**: Further optimize for low-connectivity areas

## Security Considerations for Production

1. Use environment variables for sensitive configuration
2. Implement rate limiting for API endpoints
3. Add CSRF protection
4. Use HTTPS in production
5. Implement proper logging and monitoring
6. Consider using bcrypt instead of SHA-256 for password hashing

## Support

For issues or questions about this implementation, refer to:
- Flask Documentation: https://flask.palletsprojects.com/
- SQLite Documentation: https://sqlite.org/docs.html