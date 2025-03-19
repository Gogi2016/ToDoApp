# Agile Planning Document

## 1. User Stories Table


| Story ID | User Story | Acceptance Criteria | Priority (High/Medium/Low) |
|----------|------------|---------------------|----------------------------|
| US-001 | As a user, I want to add tasks so that I can keep track of my to-dos. | Task is added successfully with title, description, and due date. | High |
| US-002 | As a user, I want to view a list of my tasks so that I can manage them. | Display tasks in a list format with task name, description, and due date. | High |
| US-003 | As a user, I want to edit my tasks so that I can update them if necessary. | Task edits are saved successfully with updated title, description, and due date. | High |
| US-004 | As a user, I want to mark tasks as completed so that I can track my progress. | Task can be marked as completed with a visual change (e.g., strikethrough). | High |
| US-005 | As a user, I want to delete tasks so that I can remove tasks I no longer need. | Task is deleted successfully with no impact on the other tasks. | Medium |
| US-006 | As a user, I want to view tasks by due date so that I can organize tasks by priority. | Tasks are sorted by due date, and upcoming tasks appear at the top. | High |
| US-007 | As a user, I want to filter tasks by their completion status so that I can view pending or completed tasks separately. | Filter works for completed and incomplete tasks. | Medium |
| US-008 | As a user, I want to save tasks locally so that my tasks are stored even if the app is closed. | Tasks should persist locally and load upon reopening the app. | High |


### 2. Product Backlog Creation


**Product Backlog Table:**

| Story ID | User Story | Priority (MoSCoW) | Effort Estimate | Dependencies |
|----------|------------|-------------------|-----------------|--------------|
| US-001 | Add tasks | Must-have | 3 | None |
| US-002 | View tasks | Must-have | 3 | None |
| US-003 | Edit tasks | Should-have | 2 | US-001 |
| US-004 | Mark tasks as completed | Must-have | 3 | US-001, US-002 |
| US-005 | Delete tasks | Should-have | 2 | US-001 |
| US-006 | View tasks by due date | Must-have | 5 | US-001, US-002 |
| US-007 | Filter tasks by status | Should-have | 3 | US-001, US-002 |
| US-008 | Save tasks locally | Must-have | 5 | US-001 |


### 3. Sprint Planning

**Selected Stories for Sprint:**

| Story ID | User Story | Task Breakdown |
|----------|------------|----------------|
| US-001 | Add tasks | Task ID: T-001 – Develop UI for adding tasks. <br> Task ID: T-002 – Implement functionality to save tasks locally. |
| US-002 | View tasks | Task ID: T-003 – Design UI for task list display. <br> Task ID: T-004 – Implement task fetching and displaying logic. |
| US-003 | Edit tasks | Task ID: T-005 – Design UI for task editing form. <br> Task ID: T-006 – Implement functionality to edit tasks locally. |
| US-004 | Mark tasks as completed | Task ID: T-007 – Design UI for marking tasks completed. <br> Task ID: T-008 – Implement functionality to update task status. |

**Sprint Backlog Table:**

| Task ID | Task Description | Assigned To | Estimated Hours | Status (To Do/In Progress/Done) |
|---------|------------------|------------|-----------------|---------------------------------|
| T-001   | Develop UI for adding tasks | Dev Team | 4 | To Do |
| T-002   | Implement functionality to save tasks locally | Dev Team | 6 | To Do |
| T-003   | Design UI for task list display | Dev Team | 5 | To Do |
| T-004   | Implement task fetching and displaying logic | Dev Team | 6 | To Do |
| T-005   | Design UI for task editing form | Dev Team | 4 | To Do |
| T-006   | Implement functionality to edit tasks locally | Dev Team | 5 | To Do |
| T-007   | Design UI for marking tasks completed | Dev Team | 3 | To Do |
| T-008   | Implement functionality to update task status | Dev Team | 5 | To Do |



## 4. Reflection

As the only stakeholder in this project, I faced challenges in prioritizing the user stories based on what would be most useful for the end-users, even though I am not yet collecting feedback from actual users. Additionally, aligning Agile practices with the project’s timeline and resources was difficult. The MoSCoW prioritization was particularly useful, though I had to be careful in estimating effort and ensuring that I focused on the most critical features for the MVP.
