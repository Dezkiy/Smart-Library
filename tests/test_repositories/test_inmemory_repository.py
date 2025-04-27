# tests/test_inmemory_generic_repository.py

from repositories.inmemory.inmemory_repository import InMemoryGenericRepository

def test_inmemory_generic_repository_crud():
    repo = InMemoryGenericRepository()

    # Dummy entities
    entity1 = {"name": "Entity One"}
    entity2 = {"name": "Entity Two"}

    # Save entities
    repo.save(entity1, id="E1")
    repo.save(entity2, id="E2")

    # Find by ID
    assert repo.find_by_id("E1") == entity1
    assert repo.find_by_id("E2") == entity2

    # Find all
    all_entities = repo.find_all()
    assert len(all_entities) == 2
    assert entity1 in all_entities
    assert entity2 in all_entities

    # Delete
    repo.delete("E1")
    assert repo.find_by_id("E1") is None
    assert len(repo.find_all()) == 1
