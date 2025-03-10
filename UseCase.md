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

## Key Actors:
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

## Use Case: Add Task
Actor: User
Precondition: User is logged in.
Postcondition: A new task is added.

## Basic Flow:
-User enters task details.
-System saves task to local storage.
-Task appears on the dashboard.

Alternative Flow: If input is empty, the system shows an error message.

## Use Case: Edit Task
Actor: User
Precondition: Task exists.
Postcondition: Task details are updated.

## Basic Flow:
-User selects a task.
-User updates task details.
-System saves changes.

Alternative Flow: If no changes are made, the system does nothing.

## Use Case: Delete Task

Actor: User
Precondition: Task exists.
Postcondition: Task is removed.

## Basic Flow:

-User selects a task.
-User confirms deletion.
-System removes the task.

Alternative Flow: If user cancels, the task remains.

## Use Case: Mark Task as Complete

Actor: User
Precondition: Task exists.
Postcondition: Task is marked complete.

Basic Flow:
-User selects a task.
-System updates task status.

Alternative Flow: If task is already complete, no change occurs.

## Use Case: Delete Account

Actor: User 
Precondition: User is logged in.
Postcondition: Account is permanently deleted.

## Basic Flow:
-User requests account deletion.
-System confirms action.
-System removes all user data from local storage.

Alternative Flow: If the user cancels, account remains active.

3. Test Cases

Test Case ID

Requirement ID

Description

Steps

Expected Result

Actual Result

Status

TC-001

FR-001

User registers

1. Enter details 2. Click Register

Account created



Pending

TC-002

FR-002

User logs in

1. Enter credentials 2. Click Login

User accesses tasks



Pending

TC-003

FR-003

User resets password

1. Request reset 2. Enter new password

Password updated



Pending

TC-004

FR-004

User adds task

1. Enter task details 2. Click Add

Task appears



Pending

TC-005

FR-005

User edits task

1. Select task 2. Modify details

Task updated



Pending

TC-006

FR-006

User deletes task

1. Select task 2. Confirm deletion

Task removed



Pending

TC-007

FR-007

User marks task complete

1. Select task 2. Click Complete

Status updated



Pending

TC-008

FR-008

User deletes account

1. Request deletion 2. Confirm

Account removed



Pending

Non-Functional Tests:

Performance Test: System should support adding 100 tasks without lag.

Security Test: Ensure passwords are hashed before storage.
