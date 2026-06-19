# Help Desk Management API
A modern Help Desk Management Platform built with FastAPI, PostgreSQL, SQLAlchemy, Docker and GitHub Actions.

This project provides a complete ticket management workflow, including authentication, role-based access control, comments, attachments, ticket history, dashboard analytics and automated testing.

Features
Authentication & Authorization
JWT Authentication
Secure Password Hashing
Role-Based Access Control (User, Agent, Admin)
Ticket Management
Create Tickets
Assign Tickets to Agents
Update Ticket Status
Search Tickets
Filter Tickets
Sort Tickets
Pagination Support
Comments
Add Comments to Tickets
View Ticket Comments
User-Ticket Relationships
Attachments
Upload Files
Download Files
Delete Attachments
Attachment History Tracking
Dashboard
Ticket Statistics
Status Metrics
Priority Metrics
Audit Log
Ticket Creation History
Status Change History
Agent Assignment History
Comment History
Attachment Upload History
Attachment Deletion History
Infrastructure
PostgreSQL Database
SQLAlchemy ORM
Alembic Database Migrations
Docker Support
GitHub Actions CI/CD
Automated Testing with Pytest
Technology Stack
Backend
FastAPI
SQLAlchemy
Pydantic
Python 3.12
Database
PostgreSQL
Alembic
Authentication
JWT (JSON Web Tokens)
Passlib
DevOps
Docker
Docker Compose
GitHub Actions
Testing
Pytest
Project Architecture
app/
├── api/
├── core/
├── database/
├── models/
├── repositories/
├── schemas/
├── services/
├── main.py

tests/
alembic/
uploads/
Architecture Layers
API Layer

Handles HTTP requests and responses.

Service Layer

Contains business logic and application rules.

Repository Layer

Handles database operations.

Database Layer

PostgreSQL + SQLAlchemy ORM.

Installation
Clone Repository
git clone https://github.com/rmonteiror/helpdesk-platform.git

cd helpdesk-platform
Create Virtual Environment
python -m venv venv
Activate Environment

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run Database Migrations
alembic upgrade head
Start Application
uvicorn app.main:app --reload
Docker

Build and run the application:

docker-compose up --build

The API will be available at:

http://localhost:8000
API Documentation

Swagger UI:

http://localhost:8000/docs

ReDoc:

http://localhost:8000/redoc
Running Tests

Run all tests:

pytest

Or:

python -m pytest -v
CI/CD

GitHub Actions automatically:

Installs dependencies
Runs automated tests
Validates project integrity
Current Functionalities
JWT Authentication
User Management
Ticket Management
Ticket Assignment
Status Workflow
Ticket Search
Ticket Filtering
Ticket Sorting
Comments
Attachments
File Upload
File Download
Dashboard Statistics
Ticket History
PostgreSQL Integration
Docker Integration
Automated Tests
Future Improvements
SLA Management
Email Notifications
WebSocket Notifications
Asset Inventory Integration
Frontend Dashboard
Multi-Tenant Support
Author

Ramon Monteiro

GitHub:
https://github.com/rmonteiror

LinkedIn:
https://www.linkedin.com/in/ramonmonteiro
