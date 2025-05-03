from repositories.task_repository import TaskRepository
from models.task import Task
from uuid import uuid4
from typing import List

class TaskService:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    def add_task(self, title: str, description: str, user_id: str) -> Task:
        if not title:
            raise ValueError("Title is required")
        task = Task(task_id=str(uuid4()), title=title, description=description, user_id=user_id, status="incomplete")
        self.task_repo.save(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.task_repo.find_all()

    def update_task(self, task_id: str, title: str, description: str) -> Task:
        task = self.task_repo.find_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        task.title = title
        task.description = description
        self.task_repo.save(task)
        return task

    def toggle_status(self, task_id: str) -> Task:
        task = self.task_repo.find_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        task.status = "complete" if task.status == "incomplete" else "incomplete"
        self.task_repo.save(task)
        return task
