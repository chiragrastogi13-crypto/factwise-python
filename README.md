# Team Project Planner Tool

## 📌 Overview

This project implements a **Team Project Planner Tool** using **Python and Django**.
It provides APIs to manage users, teams, boards, and tasks, with data stored in **local JSON files** instead of a traditional database.

---

## 🚀 Features

* Create users
* Create teams
* Create project boards
* Add tasks to boards
* Close boards (only when all tasks are complete)

---

## 🧱 Tech Stack

* Python
* Django
* JSON (File-based storage)

---

## 🗂️ Project Structure

```
FACTWISE-PYTHON/
│
├── implementations/      # Business logic layer
│   ├── user_impl.py
│   ├── team_impl.py
│   ├── board_impl.py
│
├── planner/              # Django project
│   ├── api/
│   │   ├── views.py
│   │   ├── urls.py
│
├── db/                   # JSON storage (NOT included in submission)
│   ├── users.json
│   ├── teams.json
│   ├── boards.json
│   ├── tasks.json
│
├── out/                  # Exported files
├── README.md
├── requirements.txt
```

---

## ⚙️ How It Works

```
Client (Postman)
      ↓
Django APIs (views.py)
      ↓
Implementation Layer (Business Logic)
      ↓
JSON Files (db/)
```

---

## 🔗 API Endpoints

The following APIs are implemented:

### 1. Create User

```
POST /api/create-user/
```

### 2. Create Team

```
POST /api/create-team/
```

### 3. Create Board

```
POST /api/create-board/
```

### 4. Add Task

```
POST /api/add-task/
```

### 5. Close Board

```
POST /api/close-board/
```

---

## 📥 Example Request

### Create User

```json
{
  "name": "chirag",
  "display_name": "Chirag"
}
```

---

## 📤 Example Response

```json
{
  "id": "unique-id"
}
```

---

## 📦 Data Storage

All application data is stored in JSON files:

* `users.json`
* `teams.json`
* `boards.json`
* `tasks.json`

This approach was chosen to satisfy the requirement of using **local file storage**.

---

## ⚠️ Constraints Implemented

* User name must be unique
* Team name must be unique
* Board name must be unique within a team
* Tasks can only be added to OPEN boards
* Board can only be closed when all tasks are COMPLETE

---

## 🧠 Design Decisions

### 1. File-Based Storage

Used JSON files instead of a database as required. This keeps the system simple and lightweight.

### 2. Layered Architecture

* **Implementation Layer** → Handles business logic
* **Django Layer** → Exposes APIs

This separation improves modularity and maintainability.

### 3. UUID for IDs

All entities use UUIDs to ensure uniqueness.

---

## 🧪 Testing

The APIs were tested using **Postman** by following this workflow:

1. Create user
2. Create team
3. Create board
4. Add task
5. Close board

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install django
```

### 2. Run server

```
python manage.py runserver
```

### 3. Test APIs

Use Postman:

```
http://127.0.0.1:8000/api/
```

---

## 📌 Submission Notes

* The `db/` folder is excluded from submission
* Only source code and required files are included

---

## ✅ Conclusion

This project demonstrates:

* Clean API design
* Modular architecture
* File-based persistence
* Constraint handling
* End-to-end workflow execution

---
