import pytest
from unittest.mock import MagicMock
from services.task_service import TaskService
from models.task import Task

@pytest.fixture
def mock_repo():
    return MagicMock()

@pytest.fixture
def task_service(mock_repo):
    return TaskService(task_repo=mock_repo)

def test_create_task(task_service, mock_repo):
    # Arrange
    task = Task(task_id="1", title="Read book", description="Read Python book", user_id="user1")
    
    # Act
    task_service.create_task(task)

    # Assert
    mock_repo.save.assert_called_once_with(task)

def test_toggle_task_status(task_service, mock_repo):
    # Arrange
    task = Task(task_id="1", title="Read book", description="Read Python book", user_id="user1", status="incomplete")
    mock_repo.find_by_id.return_value = task

    # Act
    updated_task = task_service.toggle_status("1")

    # Assert
    assert updated_task.status == "complete"
    mock_repo.save.assert_called_once_with(task)

def test_toggle_task_status_task_not_found(task_service, mock_repo):
    # Arrange
    mock_repo.find_by_id.return_value = None

    # Act & Assert
    with pytest.raises(ValueError, match="Task not found"):
        task_service.toggle_status("unknown-id")
