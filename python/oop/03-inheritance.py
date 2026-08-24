"""Inheritance: a subclass reuses and extends the data and behavior of a base class."""


class Item:
    def __init__(self, title: str):
        self.title = title
        self.borrowed_by = None

    def describe(self) -> str:
        return f'{self.title}'


class Book(Item):
    def __init__(self, title: str, author: str):
        super().__init__(title)   # reuse the base's setup
        self.author = author

    def describe(self) -> str:
        return f'{self.title} by {self.author}'   # extend the base


if __name__ == '__main__':
    print(Item('Untitled').describe())
    print(Book('Dune', 'Herbert').describe())
