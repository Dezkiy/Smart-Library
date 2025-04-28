from typing import List, Optional
from src.book import Book
from repositories.book_repository import BookRepository
import sqlite3  # You could replace this with an ORM like SQLAlchemy in the future

class DatabaseBookRepository(BookRepository):
    def __init__(self, database_uri: str):
        self._database_uri = database_uri
        # You can initialize a database connection here, e.g., using sqlite3, SQLAlchemy, etc.
        self._connection = sqlite3.connect(self._database_uri)

    def save(self, book: Book) -> None:
        """
        Save a book entity to the database.
        This is a stub, in the future, we will insert the book into the database.
        """
        cursor = self._connection.cursor()
        cursor.execute('''
            INSERT INTO books (isbn, title, authors, genre, publication_year, edition, publisher, total_copies, available_copies)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (book.get_isbn(), book.get_title(), ', '.join(book.get_authors()), book.get_genre(),
              book.get_publication_year(), book.get_edition(), book.get_publisher(), 
              book.get_total_copies(), book.get_available_copies()))
        self._connection.commit()

    def find_by_id(self, id: str) -> Optional[Book]:
        """
        Find a book by its ISBN (ID).
        This is a stub, in the future, we will query the database for the book by ISBN.
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM books WHERE isbn = ?', (id,))
        row = cursor.fetchone()
        if row:
            return Book(
                isbn=row[0], title=row[1], authors=row[2].split(', '), genre=row[3],
                publication_year=row[4], edition=row[5], publisher=row[6],
                total_copies=row[7], available_copies=row[8]
            )
        return None

    def find_all(self) -> List[Book]:
        """
        Find all books in the database.
        This is a stub, in the future, we will query all books from the database.
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()
        books = []
        for row in rows:
            books.append(Book(
                isbn=row[0], title=row[1], authors=row[2].split(', '), genre=row[3],
                publication_year=row[4], edition=row[5], publisher=row[6],
                total_copies=row[7], available_copies=row[8]
            ))
        return books

    def delete(self, id: str) -> None:
        """
        Delete a book by its ISBN (ID).
        This is a stub, in the future, we will delete the book from the database.
        """
        cursor = self._connection.cursor()
        cursor.execute('DELETE FROM books WHERE isbn = ?', (id,))
        self._connection.commit()

    def find_by_title(self, title: str) -> List[Book]:
        """
        Find books by their title.
        This is a stub, in the future, we will query books from the database by title.
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM books WHERE title = ?', (title,))
        rows = cursor.fetchall()
        books = []
        for row in rows:
            books.append(Book(
                isbn=row[0], title=row[1], authors=row[2].split(', '), genre=row[3],
                publication_year=row[4], edition=row[5], publisher=row[6],
                total_copies=row[7], available_copies=row[8]
            ))
        return books

    def find_by_author(self, author: str) -> List[Book]:
        """
        Find books by their author.
        This is a stub, in the future, we will query books from the database by author.
        """
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM books WHERE authors LIKE ?', ('%' + author + '%',))
        rows = cursor.fetchall()
        books = []
        for row in rows:
            books.append(Book(
                isbn=row[0], title=row[1], authors=row[2].split(', '), genre=row[3],
                publication_year=row[4], edition=row[5], publisher=row[6],
                total_copies=row[7], available_copies=row[8]
            ))
        return books
