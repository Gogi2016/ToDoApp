from fastapi import APIRouter, HTTPException
from services.task_service import TaskService
from models.task import Task
from typing import List

task_router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

task_service = TaskService(task_repo=...)  # Inject your InMemoryTaskRepo here

@task_router.get("/", response_model=List[Task])
def get_tasks():
    return task_service.get_all_tasks()

@task_router.post("/", response_model=Task)
def create_task(title: str, description: str, user_id: str):
    try:
        return task_service.add_task(title, description, user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@task_router.put("/{task_id}", response_model=Task)
def update_task(task_id: str, title: str, description: str):
    try:
        return task_service.update_task(task_id, title, description)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@task_router.post("/{task_id}/toggle", response_model=Task)
def toggle_task_status(task_id: str):
    try:
        return task_service.toggle_status(task_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
