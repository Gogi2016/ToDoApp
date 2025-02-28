#### System Architecture: To-Do App
## Project Title: To-Do App
## Domain: Productivity Tools

## Problem Statement
The To-Do App is designed to help users manage their tasks by allowing them to create, update, and delete tasks. The system stores user data in the browser's local storage to persist tasks across sessions. The system aims to be lightweight, fast, and simple, focusing on user-friendliness.

## Individual Scope
The app is designed with individual users in mind, providing them with full control over their tasks without requiring a server-side backend.

# key components:
User Interface: Consists of the registration page, login page, password reset page, and task management page.

Data Storage: Uses the browser’s local storage to persist user information and tasks.
User Authentication: Users can register, log in, authenticate, and reset their password using their email and password.

Task Management: Users can add, edit, delete, and mark tasks as complete/incomplete.
Architectural Overview
The system uses a client-side architecture, with data being stored locally in the user’s browser.

## User Interface (UI):
Registration page for new users to sign up.
Login page for returning users to access their tasks.
Password reset page to allow users to recover or change their password.
Task management page that displays tasks and allows task manipulation.

Data Persistence:
Local Storage is used to store user data (email, password) and task data (task name, description, status).

Client-Side Logic:
JavaScript is used to handle user interactions, such as form submissions, task updates, and password reset requests.
Data is retrieved and saved using local storage APIs (localStorage.setItem() and localStorage.getItem()).

### 2. C4 Model Architecture
## 2.1 Context Diagram
   
Actors:
User: Interacts with the application via a web browser.
System:
To-Do List Web Application
External Dependencies:
Browser Local Storage (for data persistence)

## Diagram Representation:
``` mermaid
graph TD;
  User -->|Uses| ToDoApp
  ToDoApp -->|Stores data in| LocalStorage
```
## 2.2 Container Diagram
Main Containers:
Frontend (Web Application): Handles UI interactions and task management logic.
Local Storage: Used for storing user authentication data and tasks.

# Diagram Representation:
``` mermaid
graph TD
  subgraph Browser
    UI["Frontend (HTML, CSS, JavaScript)"]
  end
  subgraph Storage
    LS["Local Storage"]
  end
  UI -->|Read/Write| LS
  ```
## 2.3 Component Diagram
# Key Components:
Authentication Module: Manages user registration, login, and logout.
Password Reset Module: Allows users to recover or change their password.
Task Management Module: Allows users to add, edit, update, and delete tasks.
Local Storage Manager: Handles storing and retrieving data.

# Diagram Representation:
``` mermaid
graph TD;
  subgraph ToDoApp
    Auth[Authentication Module]
    PasswordReset[Password Reset Module]
    Task[Task Management Module]
    Storage[Local Storage Manager]
  end
  Auth -->|User Credentials| Storage
  PasswordReset -->|Updated Password| Storage
  Task -->|Task Data| Storage
  ```

## 2.4 Code Diagram
``` mermaid
classDiagram
  class ToDoApp {
    +register()
    +login()
    +logout()
    +resetPassword()
  }
  class TaskManager {
    +addTask()
    +editTask()
    +updateTask()
    +deleteTask()
  }
  class PasswordReset {
    +sendResetLink()
    +updatePassword()
  }
  class LocalStorageManager {
    +saveData()
    +retrieveData()
  }
  ToDoApp --> LocalStorageManager
  TaskManager --> LocalStorageManager
  PasswordReset --> LocalStorageManager
  ```

## Feasibility Justification
The architecture is simple and does not require any external servers or databases, which makes the project highly feasible for development with minimal overhead. The local storage solution ensures data is persisted across sessions without the need for complex backend services. This approach also allows for faster development and deployment.

### 3. Technology Stack
Frontend: HTML, CSS, JavaScript
Storage: Local Storage (Browser-based)

### 4. Future Enhancements
Implement a backend with Firebase or Node.js for more advanced features like password reset and user management.
Add reminders and notifications.
Introduce task categorization and priorities.
Develop a mobile app version.




