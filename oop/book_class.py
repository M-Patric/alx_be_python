# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to notify when a book object is deleted"""
        try:
            print(f"Deleting {self.title}")
        except AttributeError:
            # If attributes are missing during deletion
            print("Deleting book instance")

    def __str__(self):
        """Human-readable string representation"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation (for debugging/recreating object)"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
