## 📦 Domain Model

| Entity  | Attributes                        | Methods                            | Relationships                             |
|---------|-----------------------------------|-------------------------------------|-------------------------------------------|
| User    | userId, name, email, password     | register(), login(), resetPassword()| 1 User can have many Tasks                |
| Task    | taskId, title, description, status| addTask(), editTask(), deleteTask()| Belongs to one User                       |
| Session | sessionId, startTime, endTime     | startSession(), endSession()        | Associated with User                      |
| Log     | logId, action, timestamp          | createLog()                         | Related to User actions                   |
| Admin   | adminId, permissions              | manageUsers(), deleteAccount()      | Inherits from User                        |
| Notification | notificationId, message, seen | sendNotification(), markAsRead()   | Sent to User                              |
