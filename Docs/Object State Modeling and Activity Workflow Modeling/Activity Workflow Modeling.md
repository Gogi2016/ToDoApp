## User Registration Workflow

```mermaid
graph TD;
    Start -->|Enter Details| Validate;
    Validate -->|Email Exists?| Exists{Yes};
    Exists -->|Show Error| End;
    Exists -->|No| SaveUser;
    SaveUser -->|Send Confirmation Email| Confirm;
    Confirm -->|User Clicks Link| Activate;
    Activate -->|Account Created| End;
```

#### Explanation
- Ensures valid email registration.
- Prevents duplicate accounts.
- Functional Requirement Mapping: FR-001 (User Registration)

## Task Addition Workflow

```mermaid
graph TD;
    Start -->|User Clicks Add Task| FormOpen;
    FormOpen -->|Enters Task Details| Validate;
    Validate -->|Valid?| Decision{Yes};
    Decision -->|No| ShowError;
    Decision -->|Yes| SaveTask;
    SaveTask -->|Task Added| End;
```

#### Explanation
- Ensures valid task creation.
- Functional Requirement Mapping: FR-002 (Task Management)
