# To-Do App

Welcome to the To-Do App, your personal task management tool! This app helps you stay organized by allowing you to register, log in, reset your password, manage your tasks and delete account. It’s a simple, user-friendly application that allows you to track and organize your daily tasks.

## Features

- **Registration and Login**: Users can register an account and log in to access their personal task list.
- **Password Reset:** Users can reset their password if they forget it, using their email and the browser's local storage.
- **Task Management**: Add, edit, delete, and update the status of your tasks.
- **Task Status**: Tasks can be marked as "complete" or "incomplete".
- **Local Storage**: All data is saved using the browser's `localStorage`, ensuring persistence between sessions.
- **Delete Account**: Account deleted will be permanantley delete on localStorage.

## How to Use

1. **Welcome Page**: Upon visiting the app, you will be greeted with the welcome page. Here, you can either **Register** or **Login** to get started.
   
2. **Register**: 
    - To create an account, click on the **Register** button and enter your name, email, and password.
    - If your email is already registered, the app will alert you that the user already exists.
   
3. **Login**: 
    - Once registered, you can log in by entering your email and password.
    - If login is successful, you will be redirected to the task management page.

4. **Manage Tasks**:
    - **Add New Task**: After logging in, you can add new tasks by clicking the **Add New Task** button and filling out the task name and description.
    - **Task Actions**: For each task, you can:
        - **Edit**: Update the task name and description.
        - **Update Status**: Toggle the status between "completed" and "incomplete".
        - **Delete**: Remove a task from the list.

5. **Logout**: 
    - When you're finished, you can log out and return to the login screen.
  
6. **Password Reset**
    - If you forget your password, you can reset it via the Forgot Password link on the login 
    page. You will be able to reset your password through local storage (without a backend service)

7.  **Delete Account**:
    - You can Delete your account and can can be deleted to localStorage too.
   
## Installation

### Prerequisites

- Web browser (Chrome, Firefox, etc.)

### Steps to Run Locally

1. Clone or download the repository:
   git clone https://github.com/Gogi2016/ToDoApp.git
   
### Links

  ##### WebApp live link : [https://gogi2016.github.io/ToDoApp/]

- [SPECIFICATION.md](SPECIFICATION.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [Reflection.md](Reflection.md)
- [StakeholderAnalysis.md](StakeholderAnalysis.md)
- [SystemRequirement.md](SystemRequirementDocument.md)
- [UseCase.md](UseCase.md)
