# Placement Portal Application V2

A full-stack Placement Management Portal developed using Flask and Vue.js. The system connects Students, Companies, and Administrators through role-based dashboards and provides placement management, job applications, analytics, notifications, report generation, ATS-style resume screening, and Progressive Web App support.

---

## Project Overview

The Placement Management Portal is designed to digitize and simplify the campus placement process.

The system provides:

- Student registration and profile management
- Company registration and admin approval
- Student approval and deactivation
- JWT-based authentication
- Role-based authorization
- Job posting and job management
- Student job applications
- Application status management
- Interview scheduling
- Candidate feedback
- Offer and placement tracking
- Notifications
- Admin and public analytics dashboards
- CSV, PDF and HTML reports
- Monthly background report generation
- ATS-style resume screening
- Progressive Web App (PWA) support
- Responsive Bootstrap UI

---

## Technology Stack

### Backend

- Python
- Flask
- Flask-JWT-Extended
- Flask-CORS
- SQLAlchemy
- SQLite
- Celery
- Redis

### Frontend

- Vue.js
- Vite
- Axios
- Bootstrap 5
- Bootstrap Icons
- Chart.js
- vue-chartjs

### PWA

- Vite PWA
- Web App Manifest
- Service Worker
- Installable application support

---

## System Architecture

```text
                         Vue.js Frontend
                                |
                              Axios
                                |
                                v
                         Flask REST API
                                |
                 +--------------+--------------+
                 |                             |
                 v                             v
            SQLAlchemy                       Celery
                 |                             |
                 v                             v
              SQLite                        Redis
                                               |
                                               v
                                         Celery Worker
                                               |
                                               v
                                      Background Tasks
