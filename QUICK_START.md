# 🚀 NavDisha-Interns Quick Start Guide

**Get your PM Internship Scheme platform running in 5 minutes!**

## 📎 Prerequisites
- Python 3.7+
- Web browser
- Internet connection (for initial setup)

## ⚡ Quick Setup

### 1. Clone & Navigate
```bash
git clone https://github.com/harjot008/NAVHAM.git
cd NAVHAM
git checkout Complete-project
```

### 2. Install Dependencies
```bash
# Create virtual environment (recommended)
python -m venv navham_env

# Activate it
# Windows:
navham_env\Scripts\activate
# macOS/Linux:
source navham_env/bin/activate

# Install packages
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python app.py
```

### 4. Open Your Browser
Go to: **http://localhost:5000**

## 📱 Test the System

### Create Your First Account
1. Click **"Sign Up"** tab
2. Enter email and password
3. Complete the 3-step profile form:
   - ✅ Basic Info (Name, Age, Gender)
   - ✅ Location & Education
   - ✅ Skills & Interests
4. View your personalized dashboard!

### Explore Features
- 🏠 **Dashboard**: See recommended internships
- ✏️ **Edit Details**: Update your profile
- 🔍 **All Internships**: Browse and filter opportunities
- 📞 **Help & Support**: Get assistance

## 🎆 Key Features

### 🤖 AI Recommendations
Get top 5 internships based on:
- 📍 Your location (state/city)
- 💼 Your skills and interests
- 🏭 Preferred sectors
- 💰 Stipend preferences

### 📱 Mobile-First Design
- Works perfectly on phones
- Fast loading for rural areas
- Simple UI for first-time users
- Touch-friendly interface

### 🔍 Advanced Search
- Filter by state, sector, keywords
- Sort by stipend, duration, location
- Real-time search results
- One-click applications

## 📈 Sample Data Included

The system comes with **30+ realistic internships** across:
- 💻 IT & Technology (8 internships)
- 🌱 Agriculture & Rural Development (7 internships)
- 🏥 Healthcare & Education (8 internships)
- 💼 Business & Finance (4 internships)
- ♾️ Environment & Energy (3 internships)

## 🚫 Troubleshooting

### Port Already in Use?
```bash
# Try a different port
python -c "from app import app; app.run(port=5001)"
# Then go to http://localhost:5001
```

### Database Issues?
```bash
# Reset database
rm internships.db
python app.py  # Will recreate automatically
```

### Import Errors?
```bash
# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

## 👥 User Flow

```
🏠 Landing Page 
    ↓
📝 Register/Login
    ↓
📋 Complete Profile (3 steps)
    ↓
🏠 Dashboard (with recommendations)
    ↓
🔍 Browse All Internships
    ↓
📧 Apply for Internships
```

## 📦 What's Included

```
NAVHAM/
├── 🐍 app.py                    # Main Flask app
├── 📜 requirements.txt         # Dependencies
├── 🗄️ internships.db           # SQLite database
├── 📋 templates/              # All HTML pages
├── 🎨 static/                 # CSS & JavaScript
├── 🗃️ models/                 # Database schema
└── 📜 Documentation files
```

## 🌐 Production Ready

For production deployment:

1. **Change secret key** in `app.py`
2. **Use PostgreSQL** instead of SQLite
3. **Enable HTTPS**
4. **Set up reverse proxy** (Nginx)
5. **Use Gunicorn** WSGI server

See `PROJECT_DOCUMENTATION.md` for detailed production setup.

## 📞 Need Help?

- 📈 **Full Documentation**: `PROJECT_DOCUMENTATION.md`
- 🐛 **Issues**: GitHub Issues tab
- 📧 **Support**: Built-in help system at `/help-support`

## 🎆 Success!

If you see the NavDisha-Interns login page at `http://localhost:5000`, you're all set!

Now create an account, complete your profile, and start exploring internship opportunities!

---

**Happy Interning! 🎉**