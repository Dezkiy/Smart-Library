# Storage Abstraction Mechanism

## Introduction

In this project, the repository layer needs to be decoupled from storage specifics. This allows for flexibility in changing storage backends without affecting the rest of the application. For this purpose, we chose to implement the **Factory Pattern** for managing repository creation.

## Choice of Design Pattern

After evaluating both **Dependency Injection (DI)** and **Factory Pattern**, we decided that the **Factory Pattern** is the best choice for this scenario due to the following reasons:

- **Simplicity**: The Factory Pattern provides a simple way to centralize and manage the creation of repositories.
- **Scalability**: It allows us to easily introduce new storage backends in the future, such as switching from an in-memory storage solution to a database-backed solution.
- **Decoupling**: By using the Factory Pattern, the repository’s storage implementation is abstracted away, allowing the service layer to interact with repositories without worrying about the underlying storage mechanism.

## Implementation Details

### Factory Pattern Overview

The **RepositoryFactory** class provides a method for creating different types of repositories based on a configuration or input string.

### Example:

```python
class RepositoryFactory:
    @staticmethod
    def get_book_repository(storage_type: str):
        if storage_type == "MEMORY":
            return InMemoryBookRepository()
        elif storage_type == "DATABASE":
            return DatabaseBookRepository()  # Future implementation
        else:
            raise ValueError("Invalid storage type")
