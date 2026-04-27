# 📊 Student Performance Analysis System

A Django-based web application for analyzing student academic performance. The system allows both students and teachers to upload and analyze Excel data, generating insights for single or multiple semesters.

---

## 🚀 Features

* 📁 Upload Excel files for analysis
* 👨‍🎓 Student performance insights
* 👩‍🏫 Teacher dashboard for multi-semester analysis
* 📊 Data visualization and reporting
* 🌐 Clean UI with static assets (CSS, JS, images)

---

## 🛠️ Tech Stack
Backend: Django (Python)
Frontend: HTML, CSS, JavaScript
Charts & Visualization: Chart.js
Database: SQLite
Libraries: pandas, numpy (for data processing)

---

## 📂 Project Structure

```
mini project/
├── myproject/
│   ├── db.sqlite3
│   ├── manage.py
│   ├── myproject/        # Django settings & configs
│   ├── static/           # CSS, JS, images, sample Excel files
│   ├── student/          # Student app
│   ├── teacher/          # Teacher app
│   └── templates/        # Base templates
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd mini-project
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

```bash
cd myproject
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 📊 Usage

* Students can upload Excel files to view performance analysis
* Teachers can:

  * Analyze single semester data
  * Compare multiple semesters
* Sample Excel files are available in:

```
static/sample/
```

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

This project is for educational purposes.

---

## 📧 Contact

For queries or suggestions, feel free to reach out.
