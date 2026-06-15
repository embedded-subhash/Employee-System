📌**Employee Management System**
📖 Overview

The Employee Management System is a Python-based console application designed using Object-Oriented Programming principles. It simulates a real-world HR backend system where employee records can be created, managed, updated, and stored persistently using JSON.

The system focuses on clean architecture, modular design, and separation of concerns, making it scalable for future enhancements such as database integration or API development.

**🎯 Objectives**
Build a structured OOP-based backend system
Implement CRUD operations for employee management
Demonstrate data persistence using JSON files
Apply real-world business logic (salary & bonus calculation)
Follow modular and maintainable coding practices
🏗️ **System Architecture**

The project follows a layered modular structure:

Model Layer → Defines Employee entity
Service Layer → Handles business logic (EmployeeManager)
Utility Layer → Provides validation and helper functions
Data Layer → Stores persistent employee records (JSON)
📂 **Project Structure**
employee_system/
│
├── main.py                      # Application entry point
│
├── models/
│   └── employee.py              # Employee class definition
│
├── services/
│   └── employee_manager.py     # Business logic (CRUD operations)
│
├── utils/
│   ├── validator.py            # Input validation utilities
│   └── helper.py               # Helper functions (timestamps, formatting)
│
├── data/
│   └── employees.json          # Persistent storage
│
└── README.md                   # Project documentation
👨‍💼 Employee Entity

Each employee record contains the following attributes:

Employee ID
Name
Email
Department
Salary
Experience (in years)
⚙️ Core Functionalities
🟢 Employee Operations
Add new employee
View all employees
Search employee by ID
Update employee details
Delete employee record
💰 Salary & Bonus System
Bonus is calculated based on experience:
Experience	Bonus Percentage
≤ 2 years	5%
≤ 5 years	10%
≤ 10 years	15%
> 10 years	20%
Final Salary = Base Salary + Bonus
Generates a formatted salary slip for each employee
💾 Data Persistence
Employee records are stored in employees.json
Data is automatically loaded when the application starts
Data is saved manually during exit or update operations
Handles missing or corrupted file scenarios gracefully
🔐**Validation Rules**
Employee ID must be unique
Salary must be non-negative
Email must contain valid format (@)
Experience must be a valid positive number
