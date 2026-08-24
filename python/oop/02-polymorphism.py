"""Polymorphism: one interface, many behaviors i.e. the same call acts differently depending on the object."""


class Item:
    def __init__(self, title: str):
        self.title = title

    def late_fee(self, days: int) -> float:
        raise NotImplementedError


class Book(Item):
    def late_fee(self, days: int) -> float:
        return days * 0.25


class DVD(Item):
    def late_fee(self, days: int) -> float:
        return days * 1.00   # DVDs cost more per day


if __name__ == '__main__':
    items = [Book('Dune'), DVD('Inception'), Book('1984')]
    for item in items:              # same loop, same call...
        print(f'{item.title}: ${item.late_fee(5):.2f}')   # ...different result