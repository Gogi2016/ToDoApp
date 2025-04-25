from typing import Optional, List
from models.task import Task
from repositories.task_repository import TaskRepository

class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self._storage = {}

    def save(self, task: Task) -> None:
        self._storage[task.id] = task

    def find_by_id(self, id: str) -> Optional[Task]:
        return self._storage.get(id)

    def find_all(self) -> List[Task]:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
