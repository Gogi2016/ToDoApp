import json
from models.task import Task
from repositories.task_repository import TaskRepository
from typing import Optional, List

class FileSystemTaskRepository(TaskRepository):
    def __init__(self, file_path: str):
        self._file_path = file_path

    def save(self, task: Task) -> None:
        tasks = self._load_all_dict()
        tasks[task.id] = task.to_dict()
        with open(self._file_path, 'w') as f:
            json.dump(tasks, f)

    def find_by_id(self, id: str) -> Optional[Task]:
        tasks = self._load_all_dict()
        task_data = tasks.get(id)
        return Task.from_dict(task_data) if task_data else None

    def find_all(self) -> List[Task]:
        tasks = self._load_all_dict()
        return [Task.from_dict(data) for data in tasks.values()]

    def delete(self, id: str) -> None:
        tasks = self._load_all_dict()
        if id in tasks:
            del tasks[id]
            with open(self._file_path, 'w') as f:
                json.dump(tasks, f)

    def _load_all_dict(self):
        try:
            with open(self._file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
