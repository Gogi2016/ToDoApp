# To-Do App

Welcome to the To-Do App, your personal task management tool! This app helps you stay organized by allowing you to register, log in, reset your password, manage your tasks and delete account. It’s a simple, user-friendly application that allows you to track and organize your daily tasks.

## Features

- **Registration and Login**: Users can register an account and log in to access their personal task list.
- **Password Reset:** Users can reset their password if they forget it, using their email and the browser's local storage.
- **Task Management**: Add, edit, delete, and update the status of your tasks.
- **Task Status**: Tasks can be marked as "complete" or "incomplete".
- **Local Storage**: All data is saved using the browser's `localStorage`, ensuring persistence between sessions.
- **Delete Account**: Account deleted will be permanently deleted on localStorage.

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
    - You can delete your account, and it will also be removed from localStorage.
   
## Installation

### Prerequisites

- Web browser (Chrome, Firefox, etc.)

### Steps to Run Locally

1. Clone or download the repository:
   ```sh
   git clone https://github.com/Gogi2016/ToDoApp.git
   ```
   
### Links

[To-Do App](https://gogi2016.github.io/ToDoApp/)

- [Agile Planning Document](Docs/Agile%20User%20Stories%2C%20Backlog%2C%20and%20Sprint%20Planning/Agile-Planning.md)
 
- [Activity Workflow Modeling](Docs/Object%20State%20Modeling%20and%20Activity%20Workflow%20Modeling/Activity%20Workflow%20Modeling.md)
- [Integration with Prior Work](Docs/Object%20State%20Modeling%20and%20Activity%20Workflow%20Modeling/Integration%20with%20Prior%20Work.md)
- [State Transition Diagrams](Docs/Object%20State%20Modeling%20and%20Activity%20Workflow%20Modeling/State%20Transition%20Diagrams.md)

- [ARCHITECTURE](Docs/Specification%20and%20%20Architectural%20Modeling/ARCHITECTURE.md)
- [SPECIFICATION](Docs/Specification%20and%20%20Architectural%20Modeling/SPECIFICATION.md)

- [Stakeholder Analysis](Docs/Stakeholder%20and%20System%20%20Requirements/StakeholderAnalysis.md)
- [System Requirement Document](Docs/Stakeholder%20and%20System%20%20Requirements/SystemRequirementDocument.md)

- [Test Case](Docs/Use%20Case%20Modeling%20and%20Test%20Case%20%20Development/TestCase.md)
- [Use Case](Docs/Use%20Case%20Modeling%20and%20Test%20Case%20%20Development/UseCase.md)

- [Domain Model](Docs/Domain%20Modeling%20and%20Class%20Diagram%20Developmen/Domain%20model.md)
- [Class Diagram](Docs/Domain%20Modeling%20and%20Class%20Diagram%20Developmen/class%20diagram.md)
