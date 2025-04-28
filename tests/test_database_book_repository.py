import unittest
from src.book import Book
from repositories.inmemory.inmemory_book_repository import InMemoryBookRepository
from repositories.database_book_repository import DatabaseBookRepository

class TestDatabaseBookRepository(unittest.TestCase):
    def setUp(self):
        """Set up a fresh repository instance before each test."""
        # You can configure the database path or URI here
        self.repo = DatabaseBookRepository(database_uri="test.db")
        
        # Alternatively, if using InMemory for faster testing
        # self.repo = InMemoryBookRepository()

        # Creating a test book to use for testing
        self.book = Book(
            isbn="12345", 
            title="Test Book", 
            authors=["Author One"], 
            genre="Fiction",
            publication_year=2022, 
            edition=1, 
            publisher="Test Publisher",
            total_copies=5, 
            available_copies=5
        )
    
    def test_save_and_find_by_id(self):
        """Test saving and finding a book by its ISBN"""
        self.repo.save(self.book)
        found_book = self.repo.find_by_id("12345")
        
        self.assertIsNotNone(found_book)  # Make sure the book was found
        self.assertEqual(found_book.get_isbn(), self.book.get_isbn())
    
    def test_find_all(self):
        """Test retrieving all books from the repository"""
        self.repo.save(self.book)
        all_books = self.repo.find_all()
        
        self.assertGreater(len(all_books), 0)  # Check that the list is not empty
    
    def test_delete(self):
        """Test deleting a book by its ISBN"""
        self.repo.save(self.book)
        self.repo.delete("12345")
        
        found_book = self.repo.find_by_id("12345")
        self.assertIsNone(found_book)  # Book should be deleted
    
    def test_find_by_title(self):
        """Test finding books by title"""
        self.repo.save(self.book)
        books = self.repo.find_by_title("Test Book")
        
        self.assertGreater(len(books), 0)  # At least one book should be found
    
    def test_find_by_author(self):
        """Test finding books by author"""
        self.repo.save(self.book)
        books = self.repo.find_by_author("Author One")
        
        self.assertGreater(len(books), 0)  # At least one book should be found

if __name__ == "__main__":
    unittest.main()
