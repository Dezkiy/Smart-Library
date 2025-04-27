# repositories/inmemory/inmemory_generic_repository.py

from typing import TypeVar, Generic, Optional, List
from repositories.repository import Repository

T = TypeVar('T')  # Entity type
ID = TypeVar('ID')  # ID type

class InMemoryGenericRepository(Repository[T, ID]):
    """
    Generic in-memory repository implementation using a dictionary (HashMap).
    """

    def __init__(self):
        self._storage = {}  # type: dict[ID, T]

    def save(self, entity: T, id: ID) -> None:
        """
        Save or update an entity with its ID.
        """
        self._storage[id] = entity

    def find_by_id(self, id: ID) -> Optional[T]:
        return self._storage.get(id)

    def find_all(self) -> List[T]:
        return list(self._storage.values())

    def delete(self, id: ID) -> None:
        if id in self._storage:
            del self._storage[id]
