from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/api/tasks/", params={
        "title": "Buy groceries",
        "description": "Milk, Eggs, Bread",
        "user_id": "user123"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Buy groceries"
    assert data["description"] == "Milk, Eggs, Bread"
    assert data["status"] == "incomplete"

def test_get_all_tasks():
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_toggle_task_status():
    # First, create a task
    create_response = client.post("/api/tasks/", params={
        "title": "Wash car",
        "description": "Exterior only",
        "user_id": "user123"
    })
    task_id = create_response.json()["task_id"]

    # Toggle the status
    toggle_response = client.post(f"/api/tasks/{task_id}/toggle")
    assert toggle_response.status_code == 200
    toggled_task = toggle_response.json()
    assert toggled_task["status"] == "complete"
