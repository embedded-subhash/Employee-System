 # Employee Management System

A Python backend project demonstrating professional REST API and software engineering practices: object-oriented design, service-layer architecture, role-based authentication, JSON data persistence, automated testing, and a Flask-based REST API.

The project has **two interfaces** built on a shared set of models and services:

1. **Console application** (`main.py`) — an interactive, menu-driven CLI for managing employees, with role-based permissions and JSON file persistence.
2. **REST API** (`app.py`) — a Flask application exposing employee CRUD operations over HTTP.

---

## Features

**Employee Management**
Add, view, search, update salary, delete, and persist employee records.

**Authentication & Role-Based Access Control**
Login system with three roles — Admin, HR, and Employee — each with different permissions (see [User Roles](#user-roles-and-permissions) below).

**Reports**
Total employee count, department-wise breakdown, highest-paid employee, average salary, and experience statistics.

**REST API**
Full CRUD over HTTP (`GET`, `POST`, `PUT`, `DELETE`) for employee records, returning JSON.

**Logging**
Application activity (logins, employee operations) is written to `logs/application.log`.

**Testing**
12 automated unit tests covering the employee model, authentication, reports, and the API layer.

---

## Technologies Used

- Python 3
- Flask (REST API)
- `unittest` / `pytest` (testing)
- JSON file storage (no database)
- Git / GitHub

---

## Project Structure

```text
Employee-System/
├── README.md
├── API_DOCUMENTATION.md
├── requirements.txt
├── app.py                      # Flask entry point — starts the REST API
├── main.py                     # Entry point — starts the console application
│
├── api/
│   └── employee_api.py         # Function-level API simulation layer (used by tests/test_api.py)
│
├── controllers/
│   └── employee_controller.py  # Flask blueprint defining the /employees routes
│
├── decorators/
│   └── permissions.py          # @admin_required — restricts an action to Admin role
│
├── models/
│   ├── employee.py             # Employee data model + validation + bonus calculation
│   └── user.py                 # User data model (username, password, role)
│
├── services/
│   ├── auth_service.py         # Login and role lookup
│   ├── employee_manager.py     # Console app's CRUD logic + JSON file persistence
│   ├── employee_service.py     # In-memory employee store backing the REST API + api/ layer
│   └── report_service.py       # Reporting calculations
│
├── utils/
│   ├── helper.py                # print_header, get_current_time
│   ├── logger.py                # File-based application logger
│   └── validator.py             # Standalone field validators
│
├── data/
│   └── employees.json          # Persisted employee records for the console app
│
├── logs/
│   ├── application.log
│   └── error.log
│
└── tests/
    ├── test_api.py
    ├── test_authentication.py
    ├── test_employee.py
    └── test_reports.py
```

> **Note on data:** the console app (`main.py`) and the REST API (`app.py`) each keep their own employee data and do **not** share state. The console app persists to `data/employees.json` across runs; the REST API stores employees in memory only and resets every time the Flask process restarts. If you need both interfaces to share one dataset, that would mean wiring `app.py` to load/save through `EmployeeManager` instead of the standalone in-memory store — currently a separate piece of work, not something this round of fixes covered.

---

## Setup & Installation

```bash
git clone https://github.com/embedded-subhash/Employee-System.git
cd Employee-System

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

---

## How to Run

**Console application:**

```bash
python main.py
```

**REST API (Flask):**

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000`. See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for endpoint details.

---

## Login Credentials (Console App)

| Role     | Username | Password  |
|----------|----------|-----------|
| Admin    | `admin`  | `admin123`|
| HR       | `hr`     | `hr123`   |
| Employee | `emp`    | `emp123`  |

## User Roles and Permissions

| Action               | Admin | HR  | Employee |
|-----------------------|:-----:|:---:|:--------:|
| View Employees         | ✅    | ✅  | ✅       |
| Search Employee        | ✅    | ✅  | ✅       |
| Add Employee           | ✅    | ✅  | ❌       |
| Update Employee Salary | ✅    | ✅  | ❌       |
| Delete Employee        | ✅    | ❌  | ❌       |
| View Reports           | ✅    | ✅  | ❌       |

---

## Testing

Run the full automated test suite:

```bash
python -m pytest tests/ -v
```

or, using only the standard library:

```bash
python -m unittest discover tests
```

All 12 tests pass: employee creation and validation, bonus calculation, login (success/wrong password/unauthorized), employee/department/average-salary reports, and the API simulation layer's create and report functions.

---

## Known Issues Fixed in This Pass

The repository had several bugs that were resolved as part of writing this documentation, so the instructions above actually work end to end:

- **`api/employee_api.py`** contained unresolved Git merge-conflict markers, which made the file a Python syntax error and broke `tests/test_api.py`. Resolved by keeping the service-layer implementation and adding a `get_employee` lookup.
- **`app.py`** referenced `employee_bp` without importing it, and duplicated the `/employees` routes inline instead of using the blueprint — it crashed on startup. Rewritten to import and register the blueprint from `controllers/employee_controller.py`.
- **`main.py`** imported `decorators.permissions`, a module that didn't exist. Added `decorators/permissions.py` with the `admin_required` decorator it needs.
- **`services/auth_service.py`** only recognized a hardcoded `admin` user and returned `True`/`False`, but `main.py` expected a `User` object with `.username` and `.role` for three different roles. Rewritten to use `models/user.py` and return proper `User` objects (or `None`) for Admin, HR, and Employee accounts.
- **`models/employee.py`** was missing `to_dict()` and `display_details()`, both of which `services/employee_manager.py` already called — saving and viewing employees in the console app crashed. Both methods were added.
- **`services/report_service.py`** was missing `total_employees`, `department_wise_report`, `highest_salary_employee`, and `experience_statistics` — all called by the console app's reports menu but never defined. Added, alongside the existing `employee_count`, `average_salary`, and `department_report` (left untouched since the test suite depends on their exact behavior).
- **`controllers/employee_controller.py`** called `service.get_all()`, `get_by_id()`, `create_employee()`, and `update_employee()` on `employee_service`, none of which existed there. Added dict-returning versions of each so the Flask blueprint works.
- **`data/employees.json`** had a syntax error (a stray, differently-shaped array spliced into the middle of the file), so loading employee data on startup failed. Fixed to valid JSON.
- **`requirements.txt`** was UTF-16 encoded and listed `requests` and its dependencies, but not `flask` (which `app.py` needs to run at all) or `pytest`. Replaced with a clean UTF-8 file listing the actual dependencies.

All of the above were verified by running the full test suite, exercising every REST endpoint with `curl`, and walking through the console app's full menu (login, add, view, reports, search, role-restricted delete, save & exit) for all three roles.

---

## Git Workflow

```bash
git checkout -b feature/rest-api-testing
git add .
git commit -m "fix: resolve merge conflict and broken imports in api layer"
git commit -m "fix: align services/controllers and add missing report/model methods"
git commit -m "docs: add README and API documentation"
git push origin feature/rest-api-testing
```

Then open a pull request into `development` for review.

---

## Author

Subhash
