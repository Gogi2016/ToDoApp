# Stakeholder Analysis Table

| Stakeholder   | Role                                          | Key Concerns                             | Pain Points                              | Success Metrics                     |
|---------------|-----------------------------------------------|------------------------------------------|------------------------------------------|--------------------------------------|
| **User**      | End user who interacts with the app          | Easy task management, intuitive UI       | Lack of synchronization across devices   | High user engagement, frequent use  |
| **Admin**     | Manages app functionality and updates        | App stability, bug-free experience       | No centralized database                  | 99% uptime, fast bug fixes           |
| **Developer** | Maintains and enhances the system             | Code maintainability, feature updates    | Complexity of features, legacy code      | Clean code, efficient feature implementation |
| **Product Manager** | Oversees product roadmap and features   | Meeting deadlines, user feedback         | Lack of prioritization of features       | On-time feature releases, user satisfaction |
| **Security Officer** | Ensures secure data management         | Data protection, secure authentication   | Vulnerabilities in user data storage     | No security breaches, encrypted data |
| **Quality Assurance** | Ensures app functions as intended      | Bug-free experience, high usability      | Unclear requirements, lack of testing    | 100% test coverage, no critical bugs  |


## 1. Functional Requirements

a. **User Authentication**: 
   - The system shall allow users to register with a name, email, and password.
   - The system shall allow users to log in using their email and password.
   - The system shall allow users to reset their password via the password reset functionality.

b. **Task Management**:
   - The system shall allow users to add new tasks with a title and description.
   - The system shall allow users to edit existing tasks.
   - The system shall allow users to delete tasks.
   - The system shall allow users to mark tasks as "completed", "incomplete", or "stuck".

c. **Account Management**:
   - The system shall allow users to delete their account and all associated data permanently.

### Acceptance Criteria for Critical Requirements:
- **Task Status**: Tasks must be updated and reflected immediately in the UI without reloading the page.
- **Account Deletion**: When a user deletes their account, all associated data (tasks, preferences) must be permanently removed from local storage.


## 3. Non-Functional Requirements

### Usability
- The user interface shall be responsive and accessible on all devices (desktop, tablet, mobile).
- The system shall comply with WCAG 2.1 accessibility standards to ensure inclusivity.

### Deployability
- The system shall be deployable on any web browser (Chrome, Firefox, Safari, etc.).

### Maintainability
- The system shall use clear coding practices and be well-documented to ensure ease of maintenance.

### Scalability
- The system shall be capable of handling at least 1,000 tasks per user without performance degradation.

### Security
- User passwords shall be encrypted and stored using the latest secure hashing techniques (e.g., bcrypt).

### Performance
- Task management actions (add, update, delete) shall execute in under 2 seconds.
- The application shall load within 3 seconds for the user to interact with it.

### Reliability
- The system shall ensure that data persists across user sessions through browser local storage.

