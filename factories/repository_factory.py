# factories/repository_factory.py

from repositories.inmemory.inmemory_book_repository import InMemoryBookRepository
# from repositories.database.database_book_repository import DatabaseBookRepository  # Future implementation

class RepositoryFactory:
    @staticmethod
    def get_book_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryBookRepository()
        elif storage_type == "DATABASE":
            # Future implementation for database repository
            # return DatabaseBookRepository()
            raise NotImplementedError("Database repository is not yet implemented")
        else:
            raise ValueError(f"Invalid storage type: {storage_type}")
