# Lab 06: Object-Oriented Programming

class Book:
    """
    A class to represent a book.

    Attributes
    ----------
    title : str
        The title of the book.
    author : str
        The author of the book.
    year : int
        The year the book was published.

    Methods
    -------
    __init__(title, author, year)
        Initialize a Book object with title, author, and year.
    __str__()
        Return a formatted string representation of the book.
    """

    def __init__(self, title, author, year):
        """
        Initialize a Book object.

        Parameters
        ----------
        title : str
            The title of the book.
        author : str
            The author of the book.
        year : int
            The year the book was published.
        """
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """
        Return a formatted string representation of the book.

        Returns
        -------
        str
            A formatted string containing the book's title, author, and year.
        """
        return f'"{self.title}" by {self.author} ({self.year})'

    def get_age(self):
        """
        Calculate the age of the book based on its publication year.

        Returns
        -------
        int
            The age of the book in years, assuming the current year is 2025.
        """
        return 2025 - self.year


class EBook(Book):
    """
    A class to represent an electronic book, inheriting from Book.

    Attributes
    ----------
    title : str
        The title of the book.
    author : str
        The author of the book.
    year : int
        The year the book was published.
    file_size : int
        The size of the e-book file in megabytes.

    Methods
    -------
    __init__(title, author, year, file_size)
        Initialize an EBook object with all Book attributes plus file_size.
    __str__()
        Return a formatted string representation including file size.
    """

    def __init__(self, title, author, year, file_size):
        """
        Initialize an EBook object.

        Parameters
        ----------
        title : str
            The title of the book.
        author : str
            The author of the book.
        year : int
            The year the book was published.
        file_size : int
            The size of the e-book file in megabytes.
        """
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        """
        Return a formatted string representation of the e-book.

        Returns
        -------
        str
            The parent's string representation followed by the file size.
        """
        parent_str = super().__str__()
        return f"{parent_str} ({self.file_size} MB)"


if __name__ == '__main__':
    # Test the Book class by creating instances
    book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    print(book1)
    print(f"Age: {book1.get_age()} years\n")

    book2 = Book("1984", "George Orwell", 1949)
    print(book2)
    print(f"Age: {book2.get_age()} years\n")

    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    print(book3)
    print(f"Age: {book3.get_age()} years\n")

    # Test the EBook class with inheritance
    ebook1 = EBook("Dune", "Frank Herbert", 1965, 5)
    print(ebook1)
    print(f"Age: {ebook1.get_age()} years\n")

    ebook2 = EBook("Clean Code", "Robert C. Martin", 2008, 12)
    print(ebook2)
    print(f"Age: {ebook2.get_age()} years")
