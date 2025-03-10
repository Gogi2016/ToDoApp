 mermaid
graph TD;
  User -->|Registers| Register
  User -->|Logs in| Login
  User -->|Resets Password| ResetPassword
  User -->|Manages Tasks| TaskManagement
  User -->|Marks Task as Complete| CompleteTask
  User -->|Edits Task| EditTask
  User -->|Deletes Task| DeleteTask
  User -->|Deletes Account| DeleteAccount
  TaskManagement -->|Includes| AddTask
  TaskManagement -->|Includes| EditTask
  TaskManagement -->|Includes| DeleteTask
