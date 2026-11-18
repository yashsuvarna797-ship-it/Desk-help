# DeskHelp – Helpdesk Management System

DeskHelp is a web-based helpdesk management system built using Django. It allows users to create support tickets, track their status, and manage their support requests through a centralized platform.

The project is being developed as a way to explore backend development, Django, database management, authentication, and CRUD operations.

## Features

- **User Authentication** – User registration, login, logout, and password management.
- **Ticket Creation** – Create support tickets with a title, description, and category.
- **Ticket Management** – View, update, and delete tickets.
- **Ticket Tracking** – Track the status of submitted tickets.
- **Comments** – Add comments to tickets.
- **Ticket Filtering** – Filter and organize tickets based on their status and date.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| SQLite | Database |
| HTML | Page structure |
| CSS | Styling |
| Git & GitHub | Version control |

## Project Structure

```text
Desk-help/
│
├── mysite/
│   ├── mysite/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   ├── DeskHelp/
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   └── manage.py
│
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd Desk-help
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install django
```

### 5. Navigate to the Django project

```bash
cd mysite
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Learning Objectives

This project focuses on understanding:

- Django's Model-View-Template architecture.
- Django ORM and database relationships.
- Function-based and class-based views.
- Forms and model forms.
- User authentication and authorization.
- CRUD operations.
- HTTP requests and responses.
- Git and version control.

## Future Improvements

- Role-based access control for employees and support staff.
- Ticket assignment to support staff.
- Dedicated support staff dashboard.
- Ticket priority management.
- Search and pagination.
- Improved ticket activity history.
- Notifications for ticket status updates.

## Author

Developed as a personal learning project to improve my understanding of Python, Django, and backend web development.