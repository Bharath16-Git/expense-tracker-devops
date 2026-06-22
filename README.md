# Expense Tracker DevOps Project

## Overview

This project is a containerized Expense Tracker application built using Python Flask, PostgreSQL, Docker, and Docker Compose.

The application allows users to:

* Add expenses
* View all expenses
* Generate expense summaries
* Get spending insights by category

---

## Technologies Used

* Python 3
* Flask
* PostgreSQL
* Docker
* Docker Compose
* Git
* GitHub
* Postman

---

## Project Architecture

Postman / Browser

↓

Flask REST API

↓

PostgreSQL Database

↓

Docker Containers

---

## API Endpoints

### Home

GET /

Response:

```json
{
  "message": "Welcome to Expense Tracker API"
}
```

### Health Check

GET /health

Response:

```json
{
  "status": "healthy"
}
```

### Add Expense

POST /expense

Request:

```json
{
  "title": "Pizza",
  "amount": 20,
  "category": "Food"
}
```

### View Expenses

GET /expenses

### Expense Summary

GET /summary

### Spending Insight

GET /insight

---

## Running the Application

Clone the repository:

```bash
git clone https://github.com/Bharath16-Git/expense-tracker-devops.git
```

Navigate to the project:

```bash
cd expense-tracker-devops
```

Start containers:

```bash
docker compose up --build
```

Access application:

```text
http://localhost:5000
```

---

## Skills Demonstrated

* REST API Development
* Python Programming
* Database Integration
* PostgreSQL
* Docker Containerization
* Docker Compose
* Git Version Control
* GitHub Collaboration
* API Testing with Postman

---

## Author

Bharath Kumar Lakkakula

MS Computer Science Graduate

Seeking Cloud Engineer, DevOps Engineer, SRE, and Technical Support Opportunities
