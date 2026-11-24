# DeskHelp 🎫
### A Django-Based Helpdesk & Ticket Management System

DeskHelp is a web-based helpdesk application designed to simplify support request management. It provides a centralized platform where users can raise support tickets, communicate through comments, and track the progress of their requests.

The application also provides support staff with tools to manage tickets, monitor their status, and keep users informed through notifications.

## ✨ Features

- **User Authentication** – Secure user registration, login, and logout.
- **Ticket Management** – Create, update, view, and delete support tickets.
- **Ticket Categories** – Organize support requests based on their category.
- **Status Tracking** – Track tickets through different stages:
  - Open
  - In Progress
  - Resolved
  - Closed
- **Ticket Assignment** – Assign support requests to staff members.
- **Comments & Discussions** – Allow users and support staff to communicate within individual tickets.
- **User Profiles** – Manage profile information, including profile pictures and bios.
- **Notifications** – Keep users updated when someone comments on their tickets.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| SQLite | Database |
| HTML5 | Page structure |
| CSS3 | Styling |
| JavaScript | Client-side interactions |
| Git & GitHub | Version control |

## 📂 Project Structure

```text
Desk-help/
│
├── mysite/
│   ├── DeskHelp/
│   │   ├── migrations/
│   │   ├── static/
│   │   ├── templates/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── forms.py
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── mysite/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── manage.py
│   └── requirements.txt
│
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip
- Git

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd Desk-help
```

### 2. Navigate to the Django project

```bash
cd mysite
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Linux / macOS**
```bash
source .venv/bin/activate
```

**Windows**
```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open your browser and visit:

`http://127.0.0.1:8000/`

## 🧠 What I Learned

Building DeskHelp helped me explore several important backend development concepts:

- Django's Model-View-Template (MVT) architecture.
- Database modelling and relationships using Django ORM.
- One-to-One and Foreign Key relationships.
- User authentication and authorization.
- Handling forms and validating user input.
- Implementing CRUD operations.
- Managing file uploads and static files.
- Using Django context processors.
- Implementing a notification system.
- Deploying a Django application.

## 🔮 Future Improvements

- Role-based access control for users and support staff.
- Email notifications for ticket updates.
- Ticket search, filtering, and pagination.
- Dashboard with ticket statistics and analytics.
- Improved mobile responsiveness.

## 👨‍💻 Author

**Yash Suvarna**

A student and aspiring software developer interested in backend development, Python, Django, and building practical web applications.

---

*Built with Django and Python.*