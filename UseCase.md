 ``` mermaid
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
 ```

### Explanation

#### Key Actors:
## User: The primary actor who interacts with the app.

## Relationships:
"Task Management" includes "Add Task," "Edit Task," and "Delete Task."
"Reset Password" and "Delete Account" are standalone features.

## Stakeholder Concerns Addressed:
Ensures a clear flow of user actions.
Enables secure authentication and task tracking.

### Use Case Specifications

## Use Case: Register
Actor: User
Precondition: User is not already registered.
Postcondition: User account is created.

## Basic Flow:
-User enters email and password.
-System validates inputs.
-System saves credentials in local storage.
-System confirms registration.

Alternative Flow: If the email already exists, the system notifies the user.

## Use Case: Reset Password
Actor: User
Precondition: User has an account.
Postcondition: Password is updated.

## Basic Flow:
-User requests a password reset.
-System verifies user identity.
-User enters a new password.
-System updates local storage.

Alternative Flow: If identity cannot be verified, the reset fails.
