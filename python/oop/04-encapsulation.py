"""Encapsulation: bundle data with the methods that guard it, and control outside access to that state."""


class Account:
    def __init__(self):
        self._fines = 0.0          # _ = "internal, don't touch directly"

    def add_fine(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError('fine must be positive')
        self._fines += amount       # the guard lives with the data

    def pay(self, amount: float) -> None:
        self._fines = max(0.0, self._fines - amount)

    @property
    def balance(self) -> float:
        return self._fines          # read-only view, no setter


if __name__ == '__main__':
    acct = Account()
    acct.add_fine(2.50)
    acct.pay(1.00)
    print(f'Owed: ${acct.balance:.2f}')
    # acct.balance = 0   # AttributeError: property has no setter