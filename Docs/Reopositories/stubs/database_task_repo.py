import mysql.connector
from typing import List, Optional
from task import Task  # Assuming Task is in the task.py module

class DatabaseTaskRepository:
    def __init__(self, db_config: dict):
        # db_config should include 'host', 'user', 'password', and 'database'
        self.db_config = db_config
        self.connection = mysql.connector.connect(**self.db_config)
        self.cursor = self.connection.cursor(dictionary=True)

    def _execute_query(self, query: str, params: tuple = ()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def _fetch_query(self, query: str, params: tuple = ()) -> List[dict]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def save(self, task: Task) -> None:
        """ Create or Update a task in the database """
        query = """
            INSERT INTO tasks (id, name, description, completed)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                name = %s, description = %s, completed = %s
        """
        params = (task.id, task.name, task.description, task.completed,
                  task.name, task.description, task.completed)
        self._execute_query(query, params)

    def find_by_id(self, task_id: str) -> Optional[Task]:
        """ Find a task by its ID """
        query = "SELECT * FROM tasks WHERE id = %s"
        result = self._fetch_query(query, (task_id,))
        if result:
            return Task.from_dict(result[0])
        return None

    def find_all(self) -> List[Task]:
        """ Fetch all tasks """
        query = "SELECT * FROM tasks"
        result = self._fetch_query(query)
        return [Task.from_dict(item) for item in result]

    def delete(self, task_id: str) -> None:
        """ Delete a task by its ID """
        query = "DELETE FROM tasks WHERE id = %s"
        self._execute_query(query, (task_id,))

    def __del__(self):
        """ Ensure the connection is closed when the object is destroyed """
        self.cursor.close()
        self.connection.close()

