from typing import TypeVar, Generic, Optional, List
from abc import ABC, abstractmethod

T = TypeVar('T')  # Entity Type
ID = TypeVar('ID')  # Entity ID Type

class Repository(Generic[T, ID], ABC):
    """
    Generic interface for CRUD operations on a given entity.
    """
    @abstractmethod
    def save(self, entity: T):
        """
        Saves an entity (Create or Update).
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """
        Finds an entity by its ID.
        Returns None if no entity with the given ID exists.
        """
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[T]:
        """
        Returns a list of all entities.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: ID):
        """
        Deletes an entity by its ID.
        """
        raise NotImplementedError
