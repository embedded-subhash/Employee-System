# Employee Management System

## Project Overview

Employee Management System is a Python-based enterprise console application developed using Object-Oriented Programming principles. The system manages employee records, user authentication, role-based access control, logging, reporting, iterators, generators, and data persistence using JSON files.

This project demonstrates professional backend development concepts commonly used in enterprise applications.

---

## Features

### Employee Management

* Add Employee
* View Employees
* Search Employee
* Update Employee Salary
* Delete Employee
* Save Employee Data

### Authentication & Authorization

* User Login System
* Role-Based Access Control
* Admin Role
* HR Role
* Employee Role

### Logging

* Application Activity Logging
* Invalid Login Tracking
* Employee Operations Logging

### Reports

* Total Employees
* Department Wise Report
* Highest Salary Employee
* Average Salary
* Experience Statistics

### Advanced Python Concepts

* Custom Iterator
* Generator
* Decorators
* JSON Data Handling
* Exception Handling

---

## Technologies Used

* Python 3.x
* Git
* GitHub
* Visual Studio Code
* PostgreSQL (Learning Module)
* Virtual Environment (venv)

---

## Project Structure

```text
employee_system/
│
├── main.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── employees.json
│   └── users.json
│
├── models/
│   ├── employee.py
│   └── user.py
│
├── services/
│   ├── employee_manager.py
│   ├── auth_service.py
│   └── report_service.py
│
├── decorators/
│   └── permissions.py
│
├── utils/
│   ├── helper.py
│   ├── validator.py
│   └── logger.py
│
├── logs/
│   ├── application.log
│   └── error.log
│
└── Practice/
    ├── employee_iterator.py
    └── employee_generator.py
```

---

## User Roles

### Admin

* Add Employee
* Update Employee
* Delete Employee
* View Reports

### HR

* Add Employee
* Update Employee
* View Reports

### Employee

* View Employee Information
* Restricted from Add, Update and Delete Operations

---

## Iterator Module

Custom Employee ID Iterator implemented using:

* **iter**()
* **next**()
* StopIteration

---

## Generator Module

Employee Generator implemented using:

* yield keyword
* Memory-efficient record generation
* Processing 100000 employee records

---

## Virtual Environment Setup

Create Virtual Environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install Dependencies:

```bash
pip install requests
```

Generate Requirements File:

```bash
pip freeze > requirements.txt
```

---

## How to Run

```bash
python main.py
```

Login Credentials:

Admin

```text
Username: admin
Password: admin123
```

HR

```text
Username: hr
Password: hr123
```

Employee

```text
Username: emp
Password: emp123
```

---

## Author

Subhash

---

## Git Workflow

Feature Branch:

```bash
git checkout -b feature/authentication-logging
```

Commit Examples:

```bash
git commit -m "feat: implement role based authentication"
git commit -m "feat: add custom permission decorators"
git commit -m "feat: implement application logging"
git commit -m "feat: add employee reports module"
```
