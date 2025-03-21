# Use Case Diagram
## actor User as "User"

 ``` mermaid
 
graph TD;
  User["👤 User"] -->|Registers| Register["📝 Register"]
  User -->|Logs in| Login["🔑 Login"]
  User -->|Resets Password| ResetPassword["🔄 Reset Password"]
  User -->|Manages Tasks| TaskManagement["📋 Manage Tasks"]
  User -->|Marks Task as Complete| CompleteTask["✅ Mark Task as Complete"]
  User -->|Edits Task| EditTask["✏️ Edit Task"]
  User -->|Deletes Task| DeleteTask["🗑️ Delete Task"]
  User -->|Deletes Account| DeleteAccount["⚠️ Delete Account"]
  
  TaskManagement -->|Includes| AddTask["➕ Add Task"]
  TaskManagement -->|Includes| EditTask
  TaskManagement -->|Includes| DeleteTask


 ```

# Explanation

## Key Actors:
- **User**: The primary actor who interacts with the app.

## Relationships:
- **Task Management** includes:
  - Add Task
  - Edit Task
  - Delete Task
- **Reset Password** and **Delete Account** are standalone features.

## Stakeholder Concerns Addressed:
- Ensures a clear flow of user actions.
- Enables secure authentication and task tracking.

# Use Case Specifications

## Use Case: Register
- **Actor**: User
- **Precondition**: User is not already registered.
- **Postcondition**: User account is created.

### Basic Flow:
1. User enters email and password.
2. System validates inputs.
3. System saves credentials in local storage.
4. System confirms registration.

### Alternative Flow:
- If the email already exists, the system notifies the user.

## Use Case: Reset Password
- **Actor**: User
- **Precondition**: User has an account.
- **Postcondition**: Password is updated.

### Basic Flow:
1. User requests a password reset.
2. System verifies user identity.
3. User enters a new password.
4. System updates local storage.

### Alternative Flow:
- If identity cannot be verified, the reset fails.

## Use Case: Add Task
- **Actor**: User
- **Precondition**: User is logged in.
- **Postcondition**: A new task is added.

### Basic Flow:
1. User enters task details.
2. System saves task to local storage.
3. Task appears on the dashboard.

### Alternative Flow:
- If input is empty, the system shows an error message.

## Use Case: Edit Task
- **Actor**: User
- **Precondition**: Task exists.
- **Postcondition**: Task details are updated.

### Basic Flow:
1. User selects a task.
2. User updates task details.
3. System saves changes.

### Alternative Flow:
- If no changes are made, the system does nothing.

## Use Case: Delete Task
- **Actor**: User
- **Precondition**: Task exists.
- **Postcondition**: Task is removed.

### Basic Flow:
1. User selects a task.
2. User confirms deletion.
3. System removes the task.

### Alternative Flow:
- If user cancels, the task remains.

## Use Case: Mark Task as Complete
- **Actor**: User
- **Precondition**: Task exists.
- **Postcondition**: Task is marked complete.

### Basic Flow:
1. User selects a task.
2. System updates task status.

### Alternative Flow:
- If task is already complete, no change occurs.

## Use Case: Delete Account
- **Actor**: User
- **Precondition**: User is logged in.
- **Postcondition**: Account is permanently deleted.

### Basic Flow:
1. User requests account deletion.
2. System confirms action.
3. System removes all user data from local storage.

### Alternative Flow:
- If the user cancels, account remains active.


# Test Cases

## Test Cases

| Test Case ID | Description                      | Precondition       | Steps to Execute                              | Expected Outcome         |
|-------------|----------------------------------|--------------------|----------------------------------------------|-------------------------|
| TC-01       | User Registration               | User is not registered | 1. Enter email & password <br> 2. Click Register | User account is created |
| TC-02       | User Login                      | User is registered | 1. Enter email & password <br> 2. Click Login | User is authenticated   |
| TC-03       | Reset Password                  | User has an account | 1. Request password reset <br> 2. Verify identity <br> 3. Enter new password | Password is updated     |
| TC-04       | Add Task                         | User is logged in  | 1. Enter task details <br> 2. Click Add Task | Task appears on dashboard |
| TC-05       | Edit Task                        | Task exists        | 1. Select task <br> 2. Update details <br> 3. Save changes | Task details updated |
| TC-06       | Delete Task                      | Task exists        | 1. Select task <br> 2. Confirm deletion | Task is removed |
| TC-07       | Mark Task as Complete            | Task exists        | 1. Select task <br> 2. Click Mark Complete | Task is marked complete |
| TC-08       | Delete Account                   | User is logged in  | 1. Request account deletion <br> 2. Confirm action | Account is deleted |

