Project Title: To-Do App
Domain: Personal Productivity / Task Management
Problem Statement: The To-Do App allows users to manage tasks, authenticate and track their task history.
 Individual Scope: This web application uses the browser's local storage to manage user authentication and tasks.
C4 Diagram Structure:
Level 1 - System Context Diagram:

The system is a simple web application where a user interacts with the To-Do App.
The system interacts with Local Storage to persist tasks and authentication data.
Level 2 - Container Diagram:

Web Application (Browser): The client-side application runs in the user's browser.
Local Storage: The data is stored locally on the user's browser, keeping track of the user’s tasks and login information.
Level 3 - Component Diagram:

Login Component: Handles registration, login, and password recovery.
Task Management Component: Handles task creation, update, and deletion.
History Component: Stores and retrieves tasks from local storage.
Level 4 - Code Diagram:

This will show individual components in more detail (we can create this based on specific code implementations later).
4. To-Do App Features Breakdown
Authentication:

Register: User registers with a username and password.
Login: User logs in with the same credentials.
Forgot Password: User can reset their password.
Task Management:

Add Task: A user can create a new task with a description.
Edit Task: User can modify the task description.
Update Status: Task status can be marked as "Completed," "Incomplete," or "Stuck."
Delete Task: User can delete tasks.
History:

Local Storage: Tasks are saved in local storage, so they persist even after the user logs out or refreshes the page.
