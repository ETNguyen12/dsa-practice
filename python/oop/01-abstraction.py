"""Abstraction: expose what an object does, hide how it does it."""
from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title: str):
        self.title = title

    @abstractmethod
    def loan_period(self) -> int:
        """Days this item can be borrowed. Subclasses define the rule."""
        ...


class Book(LibraryItem):
    def loan_period(self) -> int:
        return 21


class DVD(LibraryItem):
    def loan_period(self) -> int:
        return 7


if __name__ == '__main__':
    # LibraryItem('x')  # TypeError: can't instantiate an abstract class
    for item in (Book('Dune'), DVD('Inception')):
        print(f'{item.title}: borrow for {item.loan_period()} days')