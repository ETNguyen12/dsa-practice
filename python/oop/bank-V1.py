from abc import ABC, abstractmethod
import random

CUSTOMER = 'Customer'
EMPLOYEE = 'Employee'

NEW_CUSTOMER = 1
EXISTING_ACCOUNT = 2
GET_ACCOUNT = 3
DEPOSIT = 4
WITHDRAWL = 5
BALANCE = 6
LOGOUT = 8
SHUTDOWN = 9

class User(ABC):
    def __init__(self, name: str, email: str, age: int):
        self.name = name
        self.email = email
        self.age = age
        self.role = None
        self.password = None

    @abstractmethod
    def get_role(self) -> str:
        ...


class Employee(User):
    def __init__(self, name: str, email: str, password: str, age: int):
        super().__init__(name, email, age)
        self.role = EMPLOYEE
        self.password = password

    def get_role(self) -> str:
        return self.role


class Customer(User):
    def __init__(self, name: str, email: str, password: str, age: int):
        super().__init__(name, email, age)
        self.role = CUSTOMER
        self.password = password
        self.account = None

    def get_role(self) -> str:
        return self.role


class Account():
    def __init__(self, id: int, customer: Customer, employee: Employee, deposit: float):
        self.id = id
        self.customer = customer
        self.represenative = employee
        self.balance = deposit

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if self.balance - amount < 0:
            return False
        self.balance -= amount
        return True

    def get_balance(self) -> float:
        return self.balance


class Bank:
    def __init__(self):
        self.curr_employee = None
        self.curr_account = None
        self.users = {}
        self.accounts = {}

    def register_new_account(self, customer: Customer, employee: Employee, deposit: float) -> None:
        new_id = random.randint(10000, 99999)
        while new_id in self.accounts:
            new_id = random.randint(10000, 99999)
        account = Account(new_id, customer, employee, deposit)
        customer.account = account
        self.accounts[new_id] = account
        print(f'[New Account ID: {new_id}] {customer.name}({customer.email}) - ${account.balance}')

    def register_new_user(self, role: str, name: str, email: str, password: str, age: int) -> Customer | Employee | None:
        if email in self.users:
            print('"{}" already registered in system.'.format(email))
            return None
        if role == EMPLOYEE:
            return self.register_new_employee(name, email, password, age)
        else:
            return self.register_new_customer(name, email, password, age)

    def register_new_employee(self, name: str, email: str, password: str, age: int) -> Employee:
        employee = Employee(name, email, password, age)
        self.users[email] = employee
        return employee

    def register_new_customer(self, name: str, email: str, password: str, age: int) -> Customer:
        customer = Customer(name, email, password, age)
        self.users[email] = customer
        return customer

    def get_account(self, id: int) -> Account | None:
        if id not in self.accounts:
            print('Given ID is not a valid account ID.')
        return self.accounts.get(id)

    def get_user(self, role: str, email: str, password: str) -> Customer | Employee:
        user = self.users.get(email)
        if user is None:
            print('No user account found for "{}".'.format(email))
            return None
        elif user.role != role:
            print('User does not have permissions to login for the "{}" role.'.format(role))
            return None
        elif user.password != password:
            print('Inputted password is incorrect.')
            return None
        return user

    def login_employee(self, employee: Employee) -> None:
        bank.curr_employee = employee

    def logout_employee(self) -> None:
        bank.curr_employee = None

    def login_account(self, account: Account) -> None:
        bank.curr_account = account

    def logout_account(self) -> None:
        bank.curr_account = None


if __name__ == '__main__':
    bank = Bank()
    employee1 = bank.register_new_user(EMPLOYEE, 'Ethan Nguyen', 'ethan@gmail.com', 'password1', 23)
    employee2 = bank.register_new_user(EMPLOYEE, 'Kayla Perez', 'kayla@gmail.com', 'password2', 21)
    customer1 = bank.register_new_user(CUSTOMER, 'Vy Nguyen', 'vy@gmail.com', 'password3', 50)
    bank.register_new_account(customer1, employee1, 0)

    while True:
        while bank.curr_employee is None:
            email = input('Put your employee email: ')
            password = input('Put your employee password: ')
            user = bank.get_user(EMPLOYEE, email, password)
            if user is not None:
                bank.login_employee(user)

        print()
        print(f'{NEW_CUSTOMER} - To register new customer')
        print(f'{EXISTING_ACCOUNT} - To access an exisiting account')
        print(f'{GET_ACCOUNT} - To get account ID from credentials')
        print(f'{LOGOUT} - To log out of employee account')
        print(f'{SHUTDOWN} - To shutdown banking system')
        decision = int(input(''))
        print()

        if decision == NEW_CUSTOMER:
            name = input('Enter new customer full name: ')
            email = input('Enter new customer email: ')
            password = input('Enter new customer password: ')
            age = int(input('Enter age: '))

            customer = bank.register_new_user(CUSTOMER, name, email, password, age)
            if customer is None:
                continue

            while True:
                initial_deposit = float(input('Enter your initial deposit: '))
                if initial_deposit < 0:
                    print('Initial deposit cannot be a negative dollar amount (i.e. >= $0).')
                else:
                    break

            bank.register_new_account(customer, bank.curr_employee, initial_deposit)
        elif decision == EXISTING_ACCOUNT:
            account_id = int(input('Enter your account ID: '))
            account = bank.get_account(account_id)
            if account is None:
                continue
            bank.login_account(account)

            while bank.curr_account:
                print()
                print(f'{DEPOSIT} - To deposit into account')
                print(f'{WITHDRAWL} - To withdrawl from account')
                print(f'{BALANCE} - To see balance of account')
                print(f'{LOGOUT} - To log out of customer account')
                decision = int(input(''))
                print()

                customer = bank.curr_account.customer
                if decision == DEPOSIT:
                    while True:
                        amount = float(input('Enter your deposit amount: '))
                        if amount < 0:
                            print('Deposit cannot be a negative dollar amount (i.e. >= $0).')
                        else:
                            print(f'[Account ID: {bank.curr_account.id}] {customer.name} has deposited ${amount}.')
                            bank.curr_account.deposit(amount)
                            break
                elif decision == WITHDRAWL:
                    while True:
                        balance = bank.curr_account.get_balance()
                        print(f'[ID {account_id}] - ${balance}')
                        amount = float(input('Enter your withdrawl amount: '))
                        if bank.curr_account.withdraw(amount):
                            print(f'[Account ID: {bank.curr_account.id}] {customer.name} has withdrew ${amount}.')
                            break
                        else:
                            print('Insufficient funds.')
                elif decision == BALANCE:
                    balance = bank.curr_account.get_balance()
                    print(f'[Account ID: {account_id}] {customer.name}({customer.email}) - ${balance}')
                elif decision == LOGOUT:
                    bank.logout_account()
                else:
                    print('Not a valid option.')
        elif decision == GET_ACCOUNT:
            email = input('Enter customer email: ')
            password = input('Enter customer password: ')
            customer = bank.get_user(CUSTOMER, email, password)
            if customer is None:
                continue
            if customer.account is None:
                print(f'{customer.name} has no account yet.')
                continue
            print(f'[Account ID {customer.account.id}]: {customer.name}')
        elif decision == LOGOUT:
            bank.logout_employee()
        elif decision == SHUTDOWN:
            break
        else:
            print('Not a valid option.')
