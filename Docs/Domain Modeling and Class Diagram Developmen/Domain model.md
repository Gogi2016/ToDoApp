## 1. Domain Model


| Entity        | Attributes                                      | Methods                                         | Relationships                                |
|---------------|--------------------------------------------------|-------------------------------------------------|----------------------------------------------|
| **User**      | userId, name, email, password                   | register(), login(), resetPassword(), deleteAccount() | Has many Tasks                          |
| **Task**      | taskId, title, description, status, dueDate     | addTask(), editTask(), deleteTask(), toggleStatus() | Belongs to User                          |
| **AuthSystem**| users[], currentUser                            | authenticateUser(), logout(), resetPassword()  | Maintains all user accounts and sessions     |
| **TaskManager**| tasks[]                                        | addTask(), updateTask(), removeTask()          | Manages all tasks per User                   |
| **Account**   | accountId, createdAt, isActive                  | deactivate(), activate(), deletePermanently()  | Associated with User                         |
| **Storage**   | storageType ("localStorage"), capacity          | saveData(), retrieveData(), clearData()        | Stores data for User and Task                |
| **Session**   | sessionId, startTime, endTime                   | startSession(), endSession()                   | Associated with User                         |
| **Log**       | logId, action, timestamp                        | createLog()                                    | Related to User actions                      |
| **Admin**     | adminId, permissions                            | manageUsers(), deleteAccount()                 | Inherits from User                           |
| **Notification** | notificationId, message, seen               | sendNotification(), markAsRead()               | Sent to User                                 |

### Business Rules

- A user must register before adding tasks.
- A user can only access their own tasks.
- Tasks can be either "complete" or "incomplete".
- Each user can delete their account permanently.
- Password reset is done through localStorage (no backend).
- Data persists between sessions using localStorage.