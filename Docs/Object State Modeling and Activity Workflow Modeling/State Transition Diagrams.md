## User Account State Transition Diagram

graph TD;
    Registered -->|Activates Account| Active;
    Active -->|Suspended by Admin| Suspended;
    Active -->|User Deletes Account| Deleted;
    Suspended -->|Reactivates Account| Active;
    Deleted -->|Cannot Be Restored| X;


   # Explanation

Registered: The user has signed up but hasn't activated the account.

Active: The user can log in and manage tasks.

Suspended: The admin can suspend an account.

Deleted: The user deletes their account permanently.

Functional Requirement Mapping: Ensures account management as per FR-001 (User Registration & Management). 