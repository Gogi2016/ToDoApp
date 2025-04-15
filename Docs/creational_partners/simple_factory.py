class Task:
    def __init__(self, task_type):
        self.task_type = task_type

class TaskFactory:
    @staticmethod
    def create_task(task_type):
        return Task(task_type)
