CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS candidates (
    candidate_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER UNIQUE NOT NULL,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT CHECK(gender IN ('Male','Female','Other')),
    city TEXT,
    state TEXT,
    education TEXT,
    skills TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS interests (
    interest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    interest_name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS candidate_interests (
    candidate_id INTEGER NOT NULL,
    interest_id INTEGER NOT NULL,
    PRIMARY KEY(candidate_id, interest_id),
    FOREIGN KEY(candidate_id) REFERENCES candidates(candidate_id) ON DELETE CASCADE,
    FOREIGN KEY(interest_id) REFERENCES interests(interest_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS internships (
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

CREATE TABLE IF NOT EXISTS applications (
    application_id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_id INTEGER NOT NULL,
    internship_id INTEGER NOT NULL,
    status TEXT CHECK(status IN ('Pending','Recommended','Applied','Accepted','Rejected')) DEFAULT 'Pending',
    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(candidate_id) REFERENCES candidates(candidate_id) ON DELETE CASCADE,
    FOREIGN KEY(internship_id) REFERENCES internships(internship_id) ON DELETE CASCADE
);
