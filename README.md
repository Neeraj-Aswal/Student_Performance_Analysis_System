# 📊 Student Performance Analysis System

A full-stack Django web application designed to analyze and visualize student academic performance. The system supports both students and teachers, enabling Excel-based data upload, insightful analytics, and persistent storage using a database.

---

## 🚀 Features

### 🔐 Authentication System
- User Registration & Login
- Secure session handling
- Role-based usage (Student / Teacher)

### 👨‍🎓 Student Module
- Upload personal academic data
- Analyze subject-wise performance
- Track attendance vs marks

### 👩‍🏫 Teacher Module
- Upload class Excel data
- One Semester Analysis
- Multi-Semester Comparison
- Top performers & insights

### 📊 Data Visualization
- Bar Charts (subject performance)
- Pie Charts (pass/fail ratio)
- Scatter Plots (attendance vs marks)

### 💾 Database Integration
- Stores uploaded student & teacher data
- Data linked to logged-in users
- Prevents duplicate entries

---

## 🛠️ Tech Stack

Backend: Django (Python)  
Frontend: HTML, CSS, JavaScript  
Charts: Chart.js  
Database: SQLite  
Libraries: pandas, openpyxl  

---

## 📂 Project Structure

```
mini-project/
│
├── myproject/
│   ├── manage.py
│   ├── db.sqlite3        (ignored in Git)
│   │
│   ├── myproject/        # Main project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   ├── accounts/         # Authentication (Login/Register)
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   │
│   ├── student/          # Student module
│   │   ├── views.py
│   │   └── templates/
│   │
│   ├── teacher/          # Teacher module
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── admin.py
│   │   └── migrations/
│   │
│   ├── templates/        # Global templates (landing page etc.)
│   │
│   ├── static/           # CSS, JS, images, sample files
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   └── media/            # Uploaded files (ignored in Git)
│
└── README.md
```

## ⚙️ Installation

### 1. Clone Repository
git clone <your-repo-url>  
cd mini-project  

---

### 2. Create Virtual Environment
python -m venv venv  

---

### 3. Activate Environment

Windows:
venv\Scripts\activate  

Mac/Linux:
source venv/bin/activate  

---

### 4. Install Dependencies
pip install django pandas openpyxl  

---

### 5. Run Migrations
python manage.py makemigrations  
python manage.py migrate  

---

### 6. Create Superuser (Admin Access)
python manage.py createsuperuser  

---

### 7. Run Server
python manage.py runserver  

Open in browser:
http://127.0.0.1:8000/  

---

## 📊 Usage Flow

1. Open Homepage  
2. Click Get Started  
3. Login / Register  
4. Choose Role:
   - Teacher → Upload class data  
   - Student → Upload personal data  
5. View performance dashboard  

---

## 📁 Sample Data

Available in:
static/sample/  

---

## 🔐 Admin Panel

Access:
http://127.0.0.1:8000/admin/  

Manage:
- Users  
- Student Records  

---

## ⚠️ Important Notes

- .gitignore excludes:
  - db.sqlite3  
  - venv/  
  - media/  

- Ensure Excel format matches required columns  

---

## 🤝 Contributing

Pull requests are welcome. For major updates, open an issue first.

---

## 📄 License

This project is developed for educational purposes.
