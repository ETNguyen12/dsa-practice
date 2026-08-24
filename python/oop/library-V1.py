class Customer:

    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email
        self.books = {}

class Book:
    def __init__(self, isbn: str, title: str, author: str, year: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.id = None
        self.borrowedBy = None

class Library:
    def __init__(self):
        self.curr_book_id = 1
        self.customers = {}
        self.catalog = {}
        self.checkedIn = {}
        self.checkedOut = {}

    def __repr__(self):
        lines = ['In-Stock Books: ']
        for books in self.checkedIn.values():
            for book in books:
                lines.append(f'[ID: {book.id}] {book.title}')
        lines.append('')
        return '\n'.join(lines)

    def addBook(self, isbn: str, title: str, author: str, year: int) -> None:
        book = Book(isbn, title, author, year)
        if book.title not in self.catalog:
            self.catalog[book.title] = book.isbn
        book.id = self.curr_book_id
        self.checkedIn.setdefault(book.isbn, set()).add(book)
        self.curr_book_id += 1

    def registerNewCustomer(self, name: str, age: int, email: str) -> None:
        if email in self.customers:
            print(f'Customer already registered under {email}.')
            return
        self.customers[email] = Customer(name, age, email)
        print(f'Customer now registered under {email}.')

    def getISBN(self, title: str) -> str:
        return self.catalog.get(title)

    def getBookFromLibrary(self, isbn: str) -> Book|None:
        if isbn not in self.checkedIn:
            return None
        return self.checkedIn.get(isbn).pop()

    def getBookFromCustomer(self, customer: Customer, isbn: str) -> Book|None:
        if isbn not in customer.books:
            return None
        book = customer.books[isbn]
        self.checkedOut[isbn].remove(book)
        del customer.books[isbn]
        return book

    def getCustomer(self, email: str) -> Customer:
        return self.customers.get(email)

    def checkOutBook(self, email: str, title: str,) -> None:
        customer = self.getCustomer(email)
        if not customer:
            print(f'No customer registered under {email}.')
            return 
        
        isbn = self.getISBN(title)
        if not isbn:
            print(f'Sorry {customer.name}, we do not have "{title}" in our library.')
            return

        if isbn in customer.books:
            print(f'{customer.name} already currently has a copy of "{title}" checked out.')
            return

        book = self.getBookFromLibrary(isbn)
        if not book:
            print(f'All copies of "{title}" are currently checked out.\n')
            return

        book.borrowedBy = customer
        customer.books[isbn] = book
        self.checkedOut.setdefault(isbn, set()).add(book)
        print(f'[ID: {book.id}] {book.title} is now checked out by {customer.name}.\n')
        
    def checkInBook(self, email: str, title: str,) -> None:
        customer = self.getCustomer(email)
        if not customer:
            print(f'No customer registered under {email}.')
            return 

        isbn = self.getISBN(title)
        if not isbn:
            print(f'Sorry {customer.name}, "{title}" does not belong to our library.')
            return

        if isbn not in customer.books:
            print(f'{customer.name} did not have a copy of "{title}" checked out.')
            return

        book = self.getBookFromCustomer(customer, isbn)
        book.borrowedBy = None
        self.checkedIn[isbn].add(book)
        print(f'[ID: {book.id}] {book.title} is now checked in from {customer.name}.\n')


if __name__ == '__main__':
    library = Library()
    library.registerNewCustomer('Ethan', 23, 'ethan@gmail.com')
    library.registerNewCustomer('Kayla', 21, 'kayla@gmail.com')
    print(library)

    library.addBook(
        isbn='0394900014',
        title='The Great Gatsby',
        author='F.Scott Fitzgerald',
        year=1925
    )

    library.addBook(
        isbn='1112943552',
        title='The Cat in the Hat',
        author='Dr.Seuss',
        year=1957
    )

    library.addBook(
        isbn='0060935464',
        title='To Kill a Mockingbird',
        author='Harper Lee',
        year=1960
    )

    library.addBook(
        isbn='1112943552',
        title='The Cat in the Hat',
        author='Dr.Seuss',
        year=1957
    )
    print(library)

    library.checkOutBook('kayla@gmail.com', 'The Cat in the Hat')
    print(library)

    library.checkOutBook('kayla@gmail.com', 'The Cat in the Hat')
    library.checkOutBook('ethan@gmail.com', 'The Cat in the Hat')
    print(library)

    library.checkInBook('ethan@gmail.com', 'The Cat in the Hat')
    print(library)