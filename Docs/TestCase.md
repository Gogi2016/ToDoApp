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


