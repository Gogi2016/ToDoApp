from repositories.inmemory.inmemory_task_repository import InMemoryTaskRepository
from models.task import Task

def test_crud_operations():
    repo = InMemoryTaskRepository()

    task = Task(id="1", name="Test Task", description="Test Desc", completed=False)
    repo.save(task)
    assert repo.find_by_id("1") == task

    task.name = "Updated Name"
    repo.save(task)
    assert repo.find_by_id("1").name == "Updated Name"

    all_tasks = repo.find_all()
    assert len(all_tasks) == 1

    repo.delete("1")
    assert repo.find_by_id("1") is None
