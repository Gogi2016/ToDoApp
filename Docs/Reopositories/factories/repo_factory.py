from repositories.inmemory.inmemory_task_repository import InMemoryTaskRepository
# Future imports:
# from repositories.stubs.database_task_repository import DatabaseTaskRepository
# from repositories.stubs.filesystem_task_repository import FileSystemTaskRepository

class RepositoryFactory:
    @staticmethod
    def get_task_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryTaskRepository()
        elif storage_type == "DATABASE":
            raise NotImplementedError("Database support coming soon.")
        elif storage_type == "FILESYSTEM":
            raise NotImplementedError("Filesystem support coming soon.")
        else:
            raise ValueError("Unknown storage type.")
