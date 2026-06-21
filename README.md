# Help Desk Management API

A modern Help Desk Management Platform built with FastAPI, PostgreSQL, SQLAlchemy, Docker, GitHub Actions, and Render.

This project provides a complete ticket management workflow, including authentication, role-based access control, ticket lifecycle management, comments, attachments, SLA tracking, dashboard analytics, and automated testing.

---

## Live Demo

Production deployment available on Render:

https://SEU-LINK-DO-RENDER.onrender.com

---

## Screenshots

### Swagger UI

![Swagger UI](docs/images/helpdeskmanagement.PNG)

### Ticket Management

![Tickets](docs/images/tickets.PNG)

### Dashboard Metrics

![Dashboard](docs/images/dashboard.PNG)

### Database Structure

![Database](docs/images/database.PNG)

### Development Environment

![VS Code](docs/images/vsstudiocode.PNG)

---

## Features

### Authentication & Authorization

- JWT Authentication
- Secure Password Hashing
- Role-Based Access Control (User, Agent, Admin)

### Ticket Management

- Create Tickets
- Assign Tickets to Agents
- Update Ticket Status
- Search Tickets
- Filter Tickets
- Sort Tickets
- Pagination Support

### SLA Tracking

- Automatic SLA Due Dates
- SLA Status Monitoring
- Overdue Ticket Detection

### Comments

- Add Comments to Tickets
- View Ticket Comments
- User-Ticket Relationships

### Attachments

- Upload Files
- Download Files
- Delete Attachments
- Attachment History Tracking

### Dashboard

- Ticket Statistics
- Status Metrics
- Priority Metrics
- SLA Metrics

### Audit Log

- Ticket Creation History
- Status Change History
- Agent Assignment History
- Comment History
- Attachment History

### Infrastructure

- PostgreSQL Database
- SQLAlchemy ORM
- Alembic Migrations
- Docker Support
- GitHub Actions CI/CD
- Automated Testing with Pytest

---

## Technology Stack

### Backend

- FastAPI
- SQLAlchemy
- Pydantic
- Python 3.12

### Database

- PostgreSQL
- Alembic

### Authentication

- JWT (JSON Web Tokens)
- Passlib

### DevOps

- Docker
- Docker Compose
- GitHub Actions
- Render

### Testing

- Pytest

---

## Project Architecture

```text
app/
├── api/
├── core/
├── database/
├── models/
├── repositories/
├── schemas/
├── services/
└── main.py

tests/
alembic/
uploads/
docs/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/rmonteiror/helpdesk-platform.git
cd helpdesk-platform
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/helpdesk_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Run Database Migrations

```bash
alembic upgrade head
```

### Start Application

```bash
uvicorn app.main:app --reload
```

---

## Docker

```bash
docker-compose up --build
```

---

## API Documentation

Swagger:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

## Running Tests

```bash
pytest
```

or

```bash
python -m pytest -v
```

---

## Current Functionalities

- JWT Authentication
- User Management
- Ticket Management
- Ticket Assignment
- Ticket Status Workflow
- Ticket Search
- Ticket Filtering
- Ticket Sorting
- SLA Tracking
- Dashboard Metrics
- Comments
- Attachments
- File Upload
- File Download
- Ticket History
- PostgreSQL Integration
- Docker Integration
- Automated Tests
- Cloud Deployment (Render)

---

## Future Improvements

- Email Notifications
- WebSocket Notifications
- Asset Inventory Integration
- Frontend Dashboard
- Multi-Tenant Support

---

## Author

### Ramon Monteiro

GitHub:
https://github.com/rmonteiror

LinkedIn:
https://www.linkedin.com/in/ramonmonteiro