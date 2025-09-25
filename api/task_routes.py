from fastapi import APIRouter

task_router = APIRouter()

@task_router.get("/tasks")
async def get_tasks():
    return {"tasks": []}