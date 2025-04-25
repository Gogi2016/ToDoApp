from .base_repository import Repository
from models.task import Task

class TaskRepository(Repository[Task, str]):
    pass
