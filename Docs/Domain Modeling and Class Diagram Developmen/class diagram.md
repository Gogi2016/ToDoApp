Class Diagram

```mermaid
classDiagram
class User {
  -userId: String
  -name: String
  -email: String
  -password: String
  +register()
  +login()
  +resetPassword()
  +deleteAccount()
}

class Task {
  -taskId: String
  -title: String
  -description: String
  -status: String
  -dueDate: Date
  +addTask()
  +editTask()
  +deleteTask()
  +toggleStatus()
}

class AuthSystem {
  -users: List<User>
  -currentUser: User
  +authenticateUser()
  +logout()
  +resetPassword()
}

class TaskManager {
  -tasks: List<Task>
  +addTask()
  +updateTask()
  +removeTask()
}

class Account {
  -accountId: String
  -createdAt: Date
  -isActive: Boolean
  +deactivate()
  +activate()
  +deletePermanently()
}

class Storage {
  -storageType: String
  -capacity: Number
  +saveData()
  +retrieveData()
  +clearData()
}

class Admin {
  -adminId: String
  -permissions: String
  +manageUsers()
  +deleteAccount()
}

class Notification {
  -notificationId: String
  -message: String
  -seen: Boolean
  +sendNotification()
  +markAsRead()
}
```

User "1" -- "0..*" Task : owns
User "1" -- "1" Account : has
AuthSystem "1" --> "0..*" User : manages
TaskManager "1" --> "0..*" Task : manages
User --> Storage : uses
Task --> Storage : uses
User "1" -- "0..*" Notification : receives
Admin --|> User : inherits
