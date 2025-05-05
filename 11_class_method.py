class Book:

    """A class to represent a book and track the total number of books created.
    Attributes:
        title (str): The title of the book.
    """

    total_books: int = 0

    def __init__(self, title: str):
        self.title = title
        Book.total_books += 1

    @classmethod
    def increment_book_count(cls):
        print(f'Total Books created: {cls.total_books}')


if __name__ == '__main__':
    book1 = Book('Herry Potter')
    book2 = Book('AI Basics')
    book3 = Book('Python 101')

    Book.increment_book_count()