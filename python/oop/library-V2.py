class Book:

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.id = None
        self.borrowedBy = None

    def getBorrowerName(self) -> str | None:
        return self.borrowedBy.name if self.borrowedBy else None

class Customer:

    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email
        self.books = {}

    def add_book(self, book: Book) -> None:
        self.books[book.title] = book
        book.borrowedBy = self

    def return_book(self, title: str) -> Book:
        book = self.books.pop(title)
        book.borrowedBy = None
        return book

    def has_book(self, title) -> bool:
        return title in self.books

class Library:
    def __init__(self):
        self.curr_book_id = 1
        self.customers = {}
        self.library = {}

    def __repr__(self):
        lines = ['', 'Books: ']
        for books in self.library.values():
            for book in books:
                if book.borrowedBy is None:
                    lines.append(f'[ID: {book.id}] {book.title} = Available')
                else:
                    lines.append(f'[ID: {book.id}] {book.title} = {book.getBorrowerName()}')
        lines.append('')
        return '\n'.join(lines)

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        book.id = self.curr_book_id
        self.library.setdefault(title, []).append(book)
        print(f'[ID: {book.id}] "{book.title}" has been added to library.')
        self.curr_book_id += 1

    def register_new_customer(self, name: str, age: int, email: str) -> None:
        if email in self.customers:
            print(f'Customer already registered under {email}.')
            return
        self.customers[email] = Customer(name, age, email)
        print(f'Customer now registered under {email}.')

    def get_customer(self, email: str) -> Customer | None:
        return self.customers.get(email)

    def get_book_from_library(self, title: str) -> Book | None:
        for book in self.library.get(title, []):
            if book.borrowedBy is None:
                return book
        return None

    def check_out_book(self, email: str, title: str,) -> None:
        customer = self.get_customer(email)
        if not customer:
            print(f'No customer registered under {email}.')
            return 

        if title not in self.library:
            print(f'Sorry {customer.name}, we do not have "{title}" in our library.')
            return

        if customer.has_book(title):
            print(f'{customer.name} already currently has a copy of "{title}" checked out.')
            return

        book = self.get_book_from_library(title)
        if not book:
            print(f'All copies of "{title}" are currently checked out.\n')
            return

        customer.add_book(book)
        print(f'[ID: {book.id}] "{book.title}" is now checked out by {customer.name}.\n')
        
    def check_in_book(self, email: str, title: str,) -> None:
        customer = self.get_customer(email)
        if not customer:
            print(f'No customer registered under {email}.')
            return 

        if title not in self.library:
            print(f'Sorry {customer.name}, "{title}" does not belong to our library.')
            return

        if not customer.has_book(title):
            print(f'{customer.name} did not have a copy of "{title}" checked out.')
            return

        book = customer.return_book(title)
        print(f'[ID: {book.id}] "{book.title}" is now checked in from {customer.name}.\n')


if __name__ == '__main__':
    library = Library()
    library.register_new_customer('Ethan', 23, 'ethan@gmail.com')
    library.register_new_customer('Kayla', 21, 'kayla@gmail.com')
    print(library)

    library.add_book(
        title='The Great Gatsby',
        author='F.Scott Fitzgerald',
        year=1925
    )

    library.add_book(
        title='The Cat in the Hat',
        author='Dr.Seuss',
        year=1957
    )

    library.add_book(
        title='To Kill a Mockingbird',
        author='Harper Lee',
        year=1960
    )

    library.add_book(
        title='The Cat in the Hat',
        author='Dr.Seuss',
        year=1957
    )
    print(library)

    library.check_out_book('kayla@gmail.com', 'The Cat in the Hat')
    print(library)

    library.check_out_book('kayla@gmail.com', 'The Cat in the Hat')
    library.check_out_book('ethan@gmail.com', 'The Cat in the Hat')
    print(library)

    library.check_in_book('ethan@gmail.com', 'The Cat in the Hat')
    print(library)