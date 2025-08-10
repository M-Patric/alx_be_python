# library_system.py

class Book:
    def __init__(self, title, author):
        """Base Book class with common attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation for a Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """EBook subclass with additional file size attribute."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation for an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """PrintBook subclass with additional page count attribute."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation for a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Library class using composition to hold books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added to the library.")

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
