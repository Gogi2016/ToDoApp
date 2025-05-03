from fastapi import FastAPI
from api.task_routes import task_router

app = FastAPI(
    title="ToDo App API",
    description="Manage tasks for registered users",
    version="1.0.0"
)

app.include_router(task_router)
