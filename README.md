# 🎥 MovieReviewHub - Django Edition

A web application for managing actors, movies/series, and reviews. Built using Django to practice full-stack web development with an emphasis on clean architecture, authentication, and dynamic data.

## 📌 Features Implemented

- User authentication (login/logout)
- Actor, Item (film/series), and Review models
- Automatic average rating update via Django signals
- Class-based views: `ListView`, `DetailView`, `UpdateView`
- Dynamic confirmation popups using JavaScript (toasts)
- Search functionality with plans to expand:
  - Actor search
  - Autocomplete (upcoming)
  - Term highlighting and filters (upcoming)
- Custom queryset (`popular()`) for Actor model
- Clean and styled templates with Django templating language
- Default profile image (Geralt from The Witcher 3 😎)

## 🛠️ Technologies Used

- Python 3
- Django 4+
- HTML5 / CSS3
- JavaScript (vanilla)
- SQLite (default Django DB for dev)

## 🚀 Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/OatLatteMan/django_fp.git

2. Create and acticate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
    pip install -r requirements.txt

4. Apply migrations and run the server:
    python manage.py migrate
    python manage.py runserver 127.0.0.1:2090

## Folder Structure

📦 project-root

    ┣ 📂 myproject/             # Main Django app
    ┣ 📂 templates/             # HTML templates
    ┣ 📂 static/                # CSS and JS files
    ┣ 📜 db.sqlite3             # Default database
    ┣ 📜 manage.py              # Django management script
    ┗ 📜 README.md              # Project overview

## 👤 Author:
    - GitHub [OatLatteMan](https://github.com/OatLatteMan)
    - Based in Prague, CZ
    - Always open to learning and collaboration!

## 📄 License

This project is for educational and portfolio use.
