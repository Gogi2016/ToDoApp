## User Account State Transition Diagram

```mermaid
graph TD;
    Registered -->|Activates Account| Active;
    Active -->|Suspended by Admin| Suspended;
    Active -->|User Deletes Account| Deleted;
    Suspended -->|Reactivates Account| Active;
    Deleted -->|Cannot Be Restored| X;
```

   # Explanation

Registered: The user has signed up but hasn't activated the account.

Active: The user can log in and manage tasks.

Suspended: The admin can suspend an account.

Deleted: The user deletes their account permanently.

Functional Requirement Mapping: Ensures account management as per FR-001 (User Registration & Management). 

## Task State Transition Diagram

```mermaid
graph TD;
    Created -->|User Starts Work| InProgress;
    InProgress -->|User Marks as Completed| Completed;
    InProgress -->|User Deletes| Deleted;
    Completed -->|User Deletes| Deleted;
    Deleted -->|Cannot Be Restored| X;
```

#### Explanation
- **Created**: The task is added but not started.
- **InProgress**: The task is actively being worked on.
- **Completed**: The user marks the task as done.
- **Deleted**: The task is removed permanently.
- **Functional Requirement Mapping**: FR-002 (Task Management) is satisfied
