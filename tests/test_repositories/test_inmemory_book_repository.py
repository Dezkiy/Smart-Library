import unittest
from src.book import Book
from repositories.inmemory.inmemory_book_repository import InMemoryBookRepository


class TestInMemoryBookRepository(unittest.TestCase):

    def setUp(self):
        # This method is called before each test
        self.repo = InMemoryBookRepository()

        # Creating a book object to use in tests
        self.book_1 = Book(
            title="Clean Code",
            isbn="CC001",
            publication_year=2008,
            authors=["Robert C. Martin"],
            genre="Programming",
            edition=1,
            publisher="Prentice Hall",
            total_copies=3,
            available_copies=3
        )

        self.book_2 = Book(
            title="The Pragmatic Programmer",
            isbn="TPP001",
            publication_year=1999,
            authors=["Andrew Hunt", "David Thomas"],
            genre="Software Engineering",
            edition=1,
            publisher="Addison-Wesley",
            total_copies=5,
            available_copies=5
        )

        # Saving books to repository for testing
        self.repo.save(self.book_1)
        self.repo.save(self.book_2)

    def test_save_and_find_by_id(self):
        # Test saving a book and finding by its ISBN
        found_book = self.repo.find_by_id("CC001")
        self.assertEqual(found_book, self.book_1)
        self.assertIsNotNone(found_book)

    def test_find_all(self):
        # Test retrieving all books from the repository
        all_books = self.repo.find_all()
        self.assertIn(self.book_1, all_books)
        self.assertIn(self.book_2, all_books)

    def test_find_by_title(self):
        # Test finding books by title
        books_with_title = self.repo.find_by_title("Clean Code")
        self.assertIn(self.book_1, books_with_title)

    def test_find_by_author(self):
        # Test finding books by author
        books_by_author = self.repo.find_by_author("Robert C. Martin")
        self.assertIn(self.book_1, books_by_author)

    def test_delete(self):
        # Test deleting a book by its ISBN
        self.repo.delete("CC001")
        deleted_book = self.repo.find_by_id("CC001")
        self.assertIsNone(deleted_book)

    def test_find_by_id_non_existing(self):
        # Test finding a non-existing book by id
        non_existing_book = self.repo.find_by_id("NON_EXISTING_ISBN")
        self.assertIsNone(non_existing_book)

    def test_find_by_title_non_existing(self):
        # Test finding a non-existing book by title
        books = self.repo.find_by_title("Non Existing Title")
        self.assertEqual(books, [])

    def test_find_by_author_non_existing(self):
        # Test finding a non-existing book by author
        books = self.repo.find_by_author("Non Existing Author")
        self.assertEqual(books, [])


if __name__ == "__main__":
    unittest.main()
