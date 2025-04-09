Class Diagram

```mermaid
classDiagram
%% =====================
%% Classes with attributes and methods
%% =====================

class User {
  - userId: String
  - name: String
  - email: String
  - password: String
  + register()
  + login()
  + resetPassword()
  + deleteAccount()
}

class Task {
  - taskId: String
  - title: String
  - description: String
  - status: String
  - dueDate: Date
  + addTask()
  + editTask()
  + deleteTask()
  + toggleStatus()
}

class AuthSystem {
  - users: List<User>
  - currentUser: User
  + authenticateUser()
  + logout()
  + resetPassword()
}

class TaskManager {
  - tasks: List<Task>
  + addTask()
  + updateTask()
  + removeTask()
}

class Account {
  - accountId: String
  - createdAt: Date
  - isActive: Boolean
  + deactivate()
  + activate()
  + deletePermanently()
}

class Storage {
  - storageType: String
  - capacity: Number
  + saveData()
  + retrieveData()
  + clearData()
}

class Admin {
  - adminId: String
  - permissions: String
  + manageUsers()
  + deleteAccount()
}

class Notification {
  - notificationId: String
  - message: String
  - seen: Boolean
  + sendNotification()
  + markAsRead()
}

%% =====================
%% Relationships
%% =====================

%% Association: A User owns many Tasks (1..*), and a Task belongs to one User
User "1" --> "0..*" Task : owns

%% Composition: A User has exactly one Account (strong lifecycle dependency)
User "1" *-- "1" Account : has

%% Aggregation: AuthSystem contains Users but can exist independently
AuthSystem "1" o-- "0..*" User : manages

%% Aggregation: TaskManager holds a collection of Tasks
TaskManager "1" o-- "0..*" Task : manages

%% Association: A User interacts with Storage (localStorage)
User --> Storage : uses
Task --> Storage : uses

%% Association: A User receives many notifications
User "1" --> "0..*" Notification : receives

%% Inheritance: Admin is a specialized type of User
Admin --|> User : inherits

%% Note: Storage is a shared utility class, used by both Task and User
note for Storage "Shared utility for localStorage persistence\nUsed by both Task and User"

%% Note for Account
note for Account "Account is tightly coupled to User and deleted when User is deleted"
```
