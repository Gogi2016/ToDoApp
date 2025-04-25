class Task:
    def __init__(self, id: str, name: str, description: str, completed: bool):
        self.id = id
        self.name = name
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            completed=data["completed"],
        )
