# NavDisha-Interns: Complete PM Internship Scheme Platform

## Project Overview

NavDisha-Interns is a comprehensive web application designed for the PM Internship Scheme that helps rural and urban youth find relevant internship opportunities through an AI-powered recommendation system. The platform is optimized for mobile devices and works well in low-connectivity areas.

## Features Implemented

### 🔐 Authentication System
- **User Registration**: Complete signup process with email validation
- **Secure Login**: SHA-256 password hashing with session management
- **Profile Management**: Comprehensive user profile creation and editing
- **Session Security**: Automatic logout and session protection

### 📋 Multi-Step Profile Form
- **Step 1**: Basic Information (Name, Age, Gender, Phone)
- **Step 2**: Location & Education (City, State, Education Level, College)
- **Step 3**: Skills & Interests (Skills, Sector Preferences, Experience)
- **Progressive Validation**: Real-time form validation at each step
- **Visual Progress**: Progress bar and step indicators

### 🏠 Comprehensive Dashboard
- **User Profile Sidebar**: Quick overview of user information
- **Personalized Recommendations**: Top 5 internships based on user profile
- **Quick Actions**: Edit Details and Help & Support buttons
- **Statistics**: Platform statistics and user metrics
- **Application Status**: Track applied internships

### 🎆 AI-Powered Recommendations
- **Location-Based**: Prioritizes internships in user's state/city
- **Skill Matching**: Matches user skills with internship requirements
- **Interest Alignment**: Considers selected sector preferences
- **Smart Scoring**: Combined location and skills scoring algorithm
- **Dynamic Updates**: Recommendations update when profile changes

### 🔍 Advanced Internship Search
- **Filter System**: Filter by state, sector, and keywords
- **Search Functionality**: Search through internship descriptions
- **Sorting Options**: Sort by relevance, stipend, duration, location
- **Detailed Cards**: Comprehensive internship information display
- **Application Integration**: One-click application system

### 📞 Help & Support System
- **FAQ Section**: Comprehensive frequently asked questions
- **Contact Support**: Multiple contact options (email, chat)
- **User Guides**: Step-by-step tutorials and tips
- **Quick Links**: Easy navigation to important sections
- **Resource Center**: Additional learning materials

### 📱 Mobile-First Design
- **Responsive Layout**: Works perfectly on all device sizes
- **Touch-Friendly**: Large buttons and easy navigation
- **Fast Loading**: Optimized for low-bandwidth connections
- **Progressive Enhancement**: Works without JavaScript
- **Rural-Friendly**: Simple UI for users with low digital literacy

## Technology Stack

### Backend
- **Flask 2.3.3**: Lightweight Python web framework
- **SQLite3**: Embedded database for data storage
- **Werkzeug**: WSGI utilities and security
- **Jinja2**: Template engine for dynamic content

### Frontend
- **HTML5**: Modern semantic markup
- **CSS3**: Advanced styling with Flexbox and Grid
- **JavaScript ES6**: Interactive functionality
- **FontAwesome**: Icons and visual elements
- **Google Fonts**: Poppins font for better readability

### Security Features
- **Password Hashing**: SHA-256 encryption
- **Session Management**: Secure user sessions
- **CSRF Protection**: Form security
- **Input Validation**: Client and server-side validation
- **SQL Injection Prevention**: Parameterized queries

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Candidates Table
```sql
CREATE TABLE candidates (
    candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT CHECK(gender IN ('Male','Female','Other')),
    city TEXT,
    state TEXT,
    education TEXT,
    skills TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
);
```

### Internships Table
```sql
CREATE TABLE internships (
    internship_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    sector TEXT,
    location_state TEXT,
    location_city TEXT,
    skills_required TEXT,
    stipend INTEGER,
    duration_months INTEGER
);
```

### Applications Table
```sql
CREATE TABLE applications (
    application_id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER NOT NULL,
    internship_id INTEGER NOT NULL,
    status TEXT DEFAULT 'Applied',
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(candidate_id) REFERENCES candidates(candidate_id),
    FOREIGN KEY(internship_id) REFERENCES internships(internship_id)
);
```

## File Structure

```
NAVHAM/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── internships.db                  # SQLite database
├── PROJECT_DOCUMENTATION.md        # This file
│
├── models/
│   ├── schema.sql                  # Database schema
│   └── internships_dummy_data.sql  # Sample internship data
│
├── static/
│   ├── css/
│   │   └── home.css                # Login page styles
│   └── js/
│       └── auth.js                 # Authentication JavaScript
│
└── templates/
    ├── index.html                   # Login/Register page
    ├── complete_profile.html        # Multi-step profile form
    ├── dashboard.html               # Main dashboard
    ├── edit_profile.html            # Edit profile page
    ├── internships.html             # All internships page
    ├── help_support.html            # Help and support
    └── profile.html                 # Legacy profile page
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager
- Modern web browser

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/harjot008/NAVHAM.git
   cd NAVHAM
   git checkout Complete-project
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv navham_env
   
   # Windows
   navham_env\Scripts\activate
   
   # macOS/Linux
   source navham_env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database**
   ```bash
   # The database will be automatically initialized on first run
   # To manually reset the database, delete internships.db and restart
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Application**
   - Open browser and navigate to `http://localhost:5000`
   - Create a new account or login
   - Complete your profile to get recommendations

## API Endpoints

### Authentication
| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | `/` | Home page | - |
| POST | `/register` | User registration | email, password, name |
| POST | `/login` | User login | email, password |
| GET | `/logout` | User logout | - |

### Profile Management
| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | `/complete-profile` | Profile form page | - |
| POST | `/submit-profile` | Submit profile data | All profile fields |
| GET | `/edit-profile` | Edit profile page | - |

### Dashboard & Internships
| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | `/dashboard` | Main dashboard | - |
| GET | `/internships` | All internships | state, sector, search |
| POST | `/apply-internship` | Apply for internship | internship_id |

### Support
| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | `/help-support` | Help page | - |
| GET | `/api/user-status` | Check login status | - |

## Recommendation Algorithm

The system uses a simple but effective scoring algorithm:

```python
def get_recommended_internships(candidate_id, limit=5):
    # Location scoring
    location_score = {
        'same_state': 3,
        'same_city': 2,
        'other': 1
    }
    
    # Skills matching
    skills_score = {
        'skill_match': 3,
        'no_skills_required': 1,
        'no_match': 0
    }
    
    # Combined score = location_score + skills_score + stipend_bonus
    # Results sorted by total score DESC
```

## User Journey

### New User Flow
1. **Landing Page**: User sees login/register form
2. **Registration**: User creates account with email/password
3. **Profile Completion**: Multi-step form to gather user information
4. **Dashboard**: User sees personalized recommendations
5. **Browse & Apply**: User can explore all internships and apply

### Returning User Flow
1. **Login**: User enters credentials
2. **Dashboard**: Immediate access to personalized content
3. **Updates**: User can edit profile anytime
4. **Applications**: Track application status

## Mobile Optimization

### Design Principles
- **Mobile-First**: Designed primarily for mobile users
- **Touch-Friendly**: Large buttons (minimum 44px height)
- **Fast Loading**: Minimal assets and optimized code
- **Readable Text**: 16px+ font sizes for easy reading
- **Simple Navigation**: Clear, intuitive menu structure

### Low-Connectivity Support
- **Minimal JavaScript**: Works without JS enabled
- **Compressed Assets**: Optimized images and styles
- **Efficient Database**: Fast SQLite queries
- **Caching**: Browser caching for static resources

## Testing the System

### Manual Testing Steps

1. **Registration Test**
   - Go to `http://localhost:5000`
   - Click "Sign Up" tab
   - Fill form and register
   - Verify redirection to profile completion

2. **Profile Completion Test**
   - Complete all three steps of profile form
   - Test validation on each step
   - Verify submission and redirect to dashboard

3. **Dashboard Test**
   - Check personalized recommendations
   - Test "Edit Details" button
   - Test "Help & Support" button
   - Verify user information display

4. **Internships Test**
   - Navigate to "All Internships"
   - Test filtering by state/sector
   - Test search functionality
   - Test application button

5. **Login Test**
   - Logout and login again
   - Verify session persistence
   - Test "Remember me" functionality

### Data Validation Tests
- Email format validation
- Required field validation
- Age range validation (16-30)
- State selection validation
- Skills format validation

## Production Deployment

### Security Enhancements
1. **Change Secret Key**: Update `app.secret_key` to a strong random string
2. **Environment Variables**: Use environment variables for sensitive data
3. **HTTPS**: Enable SSL/TLS encryption
4. **Rate Limiting**: Implement API rate limiting
5. **Input Sanitization**: Additional XSS protection

### Performance Optimizations
1. **Database**: Consider PostgreSQL for production
2. **Caching**: Implement Redis for session storage
3. **CDN**: Use CDN for static assets
4. **Compression**: Enable gzip compression
5. **Monitoring**: Add application monitoring

### Scaling Considerations
1. **Load Balancing**: Multiple application instances
2. **Database Sharding**: Separate read/write databases
3. **Microservices**: Split into smaller services
4. **Queue System**: Implement job queues for heavy tasks

## Future Enhancements

### Phase 2 Features
- **Advanced Filters**: More granular filtering options
- **Saved Searches**: Allow users to save search criteria
- **Email Notifications**: Automated notifications for new matches
- **Application Tracking**: Detailed application status updates
- **Company Profiles**: Detailed information about internship providers

### Phase 3 Features
- **Video Interviews**: Integrated video interview system
- **Skill Assessments**: Online skill testing and certification
- **Mentorship Program**: Connect students with industry mentors
- **Alumni Network**: Connect with past interns
- **Analytics Dashboard**: Detailed insights for administrators

### AI/ML Enhancements
- **Advanced NLP**: Better text analysis for skill matching
- **User Behavior Tracking**: Learn from user interactions
- **Predictive Analytics**: Predict application success rates
- **Chatbot Support**: AI-powered help system

## Support & Maintenance

### Regular Maintenance
- **Database Backups**: Daily automated backups
- **Security Updates**: Regular dependency updates
- **Performance Monitoring**: Track application metrics
- **User Feedback**: Regular surveys and improvements

### Support Channels
- **Email**: support@navdisha-interns.gov.in
- **Documentation**: This comprehensive guide
- **FAQ System**: Built-in help system
- **Video Tutorials**: Step-by-step guides

## Contributing

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Code Standards
- **Python**: Follow PEP 8 style guide
- **JavaScript**: Use ES6+ features
- **HTML/CSS**: Semantic markup and organized styles
- **Comments**: Document complex logic
- **Testing**: Include tests for new features

## License

This project is developed for the PM Internship Scheme and is intended for government use. All rights reserved.

## Acknowledgments

- **PM Internship Scheme**: For the initiative to help Indian youth
- **Rural Development**: Focus on bridging the digital divide
- **Open Source**: Built using open source technologies
- **Community**: Feedback from users and stakeholders

---

**Version**: 1.0.0  
**Last Updated**: September 22, 2025  
**Developer**: PM Internship Scheme Development Team