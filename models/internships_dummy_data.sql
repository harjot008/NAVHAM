-- Dummy data for internships table
-- 30 realistic internship opportunities for Indian students
-- Covers various sectors including rural development, IT, healthcare, agriculture, etc.

INSERT INTO internships (title, description, sector, location_state, location_city, skills_required, stipend, duration_months, duration_days) VALUES

-- IT and Technology Internships (8 entries)
('Web Development Intern', 'Develop responsive websites using HTML, CSS, JavaScript and work on real client projects', 'IT', 'Haryana', 'Gurgaon', 'HTML, CSS, JavaScript, React', 15000, 3, 90),
('Mobile App Development Intern', 'Create Android applications using Java/Kotlin for local businesses', 'IT', 'Karnataka', 'Bangalore', 'Java, Android Studio, Kotlin', 18000, 4, 120),
('Data Analysis Intern', 'Analyze agricultural and rural development data using Python and Excel', 'IT', 'Maharashtra', 'Pune', 'Python, Excel, SQL, Data Visualization', 12000, 2, 60),
('Digital Marketing Intern', 'Create social media campaigns for rural businesses and startups', 'Marketing', 'Delhi', 'New Delhi', 'Social Media, Content Writing, Google Analytics', 10000, 2, 60),
('Cybersecurity Intern', 'Learn network security and help secure small business IT infrastructure', 'IT', 'Tamil Nadu', 'Chennai', 'Network Security, Ethical Hacking, Linux', 16000, 3, 90),
('UI/UX Design Intern', 'Design user interfaces for mobile apps targeting rural users', 'Design', 'Telangana', 'Hyderabad', 'Figma, Adobe XD, User Research', 14000, 3, 90),
('Backend Development Intern', 'Build APIs and database systems for agricultural tech solutions', 'IT', 'West Bengal', 'Kolkata', 'Python, Django, PostgreSQL, REST APIs', 17000, 4, 120),
('Software Testing Intern', 'Test mobile applications and web platforms for rural development NGOs', 'IT', 'Gujarat', 'Ahmedabad', 'Manual Testing, Selenium, Bug Reporting', 11000, 2, 60),

-- Agriculture and Rural Development (7 entries)
('Agricultural Research Intern', 'Research sustainable farming practices and document case studies in rural areas', 'Agriculture', 'Punjab', 'Ludhiana', 'Research, Data Collection, Agricultural Knowledge', 8000, 3, 90),
('Organic Farming Intern', 'Learn and promote organic farming techniques in village communities', 'Agriculture', 'Himachal Pradesh', 'Shimla', 'Organic Farming, Community Engagement', 7000, 4, 120),
('Rural Development Intern', 'Work with NGOs to implement development projects in remote villages', 'Social Work', 'Uttar Pradesh', 'Lucknow', 'Community Work, Project Management, Hindi', 9000, 3, 90),
('Water Conservation Intern', 'Implement rainwater harvesting and irrigation efficiency projects', 'Environment', 'Rajasthan', 'Jaipur', 'Environmental Science, Project Implementation', 8500, 3, 90),
('Livestock Management Intern', 'Assist in cattle and poultry management programs for rural farmers', 'Agriculture', 'Haryana', 'Hisar', 'Animal Husbandry, Veterinary Basics, Record Keeping', 7500, 2, 60),
('Sustainable Agriculture Intern', 'Promote eco-friendly farming and help farmers adopt new technologies', 'Agriculture', 'Madhya Pradesh', 'Bhopal', 'Sustainable Practices, Farmer Training, Communication', 8000, 4, 120),
('Rural Entrepreneurship Intern', 'Help villagers start small businesses and access microfinance', 'Business', 'Bihar', 'Patna', 'Business Planning, Financial Literacy, Local Languages', 6000, 3, 90),

-- Healthcare and Education (8 entries)
('Healthcare Awareness Intern', 'Conduct health awareness programs in rural communities', 'Healthcare', 'Odisha', 'Bhubaneswar', 'Public Health, Communication, Local Language', 7000, 2, 60),
('Telemedicine Support Intern', 'Assist in providing remote healthcare services to rural areas', 'Healthcare', 'Kerala', 'Kochi', 'Basic Medical Knowledge, Technology Support', 9000, 3, 90),
('Rural Education Intern', 'Teach basic computer skills and digital literacy in village schools', 'Education', 'Assam', 'Guwahati', 'Teaching, Computer Skills, Patience', 6000, 3, 90),
('Nutrition Program Intern', 'Implement child nutrition programs in rural schools and communities', 'Healthcare', 'Chhattisgarh', 'Raipur', 'Nutrition Science, Community Health, Data Collection', 7500, 2, 60),
('Mental Health Awareness Intern', 'Create awareness about mental health in rural communities', 'Healthcare', 'Jharkhand', 'Ranchi', 'Psychology, Counseling Basics, Empathy', 6500, 2, 60),
('Adult Literacy Intern', 'Teach reading and writing to adults in rural areas', 'Education', 'Uttarakhand', 'Dehradun', 'Teaching Skills, Patience, Local Language', 5000, 4, 120),
('School Infrastructure Intern', 'Help improve basic infrastructure in rural schools', 'Education', 'Tripura', 'Agartala', 'Project Management, Basic Construction Knowledge', 6000, 2, 60),
('Mobile Health Unit Intern', 'Support mobile healthcare units serving remote villages', 'Healthcare', 'Meghalaya', 'Shillong', 'First Aid, Patient Care, Record Keeping', 7000, 3, 90),

-- Business and Finance (4 entries)
('Microfinance Intern', 'Help rural entrepreneurs access small loans and financial services', 'Finance', 'Andhra Pradesh', 'Vijayawada', 'Financial Analysis, Communication, Excel', 8000, 3, 90),
('Rural Banking Intern', 'Assist in expanding banking services to unbanked rural areas', 'Finance', 'Manipur', 'Imphal', 'Banking Operations, Customer Service, Local Language', 9000, 3, 90),
('Cooperative Management Intern', 'Help manage rural cooperatives and self-help groups', 'Management', 'Nagaland', 'Kohima', 'Group Management, Accounting, Leadership', 6000, 4, 120),
('Market Linkage Intern', 'Connect rural producers with urban markets and e-commerce platforms', 'Business', 'Mizoram', 'Aizawl', 'Market Research, Digital Platforms, Negotiation', 7000, 3, 90),

-- Environment and Renewable Energy (3 entries)
('Solar Energy Intern', 'Install and maintain solar panels in rural households and schools', 'Energy', 'Goa', 'Panaji', 'Basic Electrical, Solar Technology, Technical Skills', 10000, 3, 90),
('Environmental Conservation Intern', 'Implement tree plantation and waste management programs in villages', 'Environment', 'Arunachal Pradesh', 'Itanagar', 'Environmental Science, Community Mobilization', 6000, 2, 60),
('Renewable Energy Research Intern', 'Research feasibility of renewable energy solutions for rural areas', 'Energy', 'Sikkim', 'Gangtok', 'Research Skills, Technical Writing, Energy Systems', 8000, 4, 120);