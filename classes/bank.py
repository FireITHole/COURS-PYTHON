from datetime import datetime
from random import choices

def generate_id() -> str:
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(choices(population=chars, k=16))

class BalanceException(Exception):
    def __init__(self, message="balance is insufficient."):
        self.message = message
        super().__init__(self.message)

class Transaction:
    def __init__(self, type: str, state: str, amount: float, accountFrom: "BankAccount", accountTo: "BankAccount" = None, dateTime: datetime = datetime.now()):
        self.type = type
        self.state = state
        self.amount = amount
        self.accountFrom = accountFrom
        self.accountTo = accountTo
        self.dateTime = dateTime
        self.id = generate_id()

    def __str__(self) -> str:
        return f"ID: {self.id}\nDateTime: {self.dateTime}\nType: {self.type}\nState: {self.state}\nAmount: {self.amount:.2f}€\nAccount: {self.accountFrom.get_name()}\n"

    def get_type(self) -> str:
        return self.type

class Transfer(Transaction):
    def __init__(self, state: str, amount: float, accountFrom: "BankAccount", accountTo: "BankAccount"):
        super().__init__("transfer", state, amount, accountFrom, accountTo)

    def __str__(self):
        return f"ID: {self.id}\nDateTime: {self.dateTime}\nType: {self.type}\nState: {self.state}\nAmount: {self.amount:.2f}€\nAccountFrom: {self.accountFrom.get_name()}\nAccountTo: {self.accountTo.get_name()}\n"

class Deposit(Transaction):
    def __init__(self, state: str, amount: float, accountFrom: "BankAccount"):
        super().__init__("deposit", state, amount, accountFrom)

class Withdraw(Transaction):
    def __init__(self, state: str, amount: float, accountFrom: "BankAccount"):
        super().__init__("withdraw", state, amount, accountFrom)

class BankAccount:
    def __init__(self, bank: "Bank", name: str, initAmount: float, owner: "User"):
        self.bank = bank
        self.name = name
        self.balance = initAmount
        self.owner = owner
        self.id = generate_id()
        self.transactions: list[Transfer|Deposit|Withdraw] = []
        print(f"Account '{self.name}' successfully created at the bank '{self.bank.get_name()}' with an initial balance of {self.balance:.2f}€\n")
    
    def __sub__(self, amount: float):
        try:
            self.is_balance_sufficient(amount)
            self.balance -= amount
            self.transactions.append(Withdraw("successful", amount, self))
        except BalanceException as error:
            self.transactions.append(Withdraw("failed", amount, self))
            print(f"Couldn't remove {amount:.2f}€ from '{self.name}': {error}\n")

    def __add__(self, amount: float):
        self.balance += amount
        self.transactions.append(Deposit("successful", amount, self))

    def __str__(self) -> None:
        return f"Infos about the account '{self.name}':\n    ID: {self.id}\n    Name: {self.name}\n    Bank: {self.get_bank_name()}\n    Owner: {self.owner.get_full_name()}\n    Balance: {self.balance:.2f}€\n"

    def get_owner(self) -> "User":
        return self.owner
    
    def get_name(self) -> str:
        return self.name
    
    def get_balance(self) -> float:
        return self.balance
    
    def get_bank_name(self) -> str:
        return self.bank.get_name()
    
    def get_transactions(self) -> list[Transfer|Deposit|Withdraw]:
        return self.transactions

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.transactions.append(Deposit("successful", amount, self))
        print(f"Successfuly deposited {amount:.2f}€ to the account '{self.name}'\n")

    def is_balance_sufficient(self, amount) -> None:
        if amount > self.balance:
            raise BalanceException()

    def withdraw(self, amount: float) -> None:
        try:
            self.is_balance_sufficient(amount)
            self.balance -= amount
            self.transactions.append(Withdraw("successful", amount, self))
            print(f"Successfuly withdrawn {amount:.2f}€ from the account '{self.name}'\n")
        except BalanceException as error:
            self.transactions.append(Withdraw("failed", amount, self))
            print(f"Couldn't withdraw {amount:.2f}€ from '{self.name}': {error}\n")

    def transfert(self, amount: float, bankAccountTo: "BankAccount") -> None:
        try:
            self.is_balance_sufficient(amount)
            self.balance -= amount
            bankAccountTo + amount
            self.transactions.append(Transfer("successful", amount, self, bankAccountTo))
            print(f"Successfully transfered {amount:.2f}€ from '{self.name}' to '{bankAccountTo.get_name()}'\n")
        except BalanceException as error:
            self.transactions.append(Transfer("failed", amount, self, bankAccountTo))
            print(f"Couldn't transfer {amount:.2f}€ from '{self.name}' to '{bankAccountTo.get_name()}': {error}'\n")

class User:
    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        self.id = generate_id()
        self.bankAccounts: list[BankAccount] = []
        print(f"User '{self.get_full_name()}' successfully created.\n")
    
    def __str__(self):
        strAccounts = []
        for bankAccount in self.bankAccounts:
            strAccounts.append(f"        - {bankAccount.get_name()} @ {bankAccount.get_bank_name()}")
        strAccounts = '\n'.join(strAccounts)
        return f"Infos about the user '{self.get_full_name()}':\n    ID: {self.id}\n    First name: {self.firstName}\n    Last name: {self.lastName}\n    Bank accounts:\n{strAccounts}\n    Net worth: {self.get_net_worth():.2f}€\n"
    
    def get_full_name(self) -> str:
        return f"{self.firstName} {self.lastName}"

    def add_bank_account(self, bankAccount: BankAccount):
        self.bankAccounts.append(bankAccount)

    def get_net_worth(self) -> float:
        return sum(account.get_balance() for account in self.bankAccounts)
    
class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
        print(f"Bank '{self.name}' successfully created.\n")
    
    def __str__(self) -> None:
        users_loop = []
        for user in {account.get_owner() for account in self.accounts}:
            users_loop.append(f"        {user.get_full_name()}:")
            for account in self.get_accounts_from_user(user):
                users_loop.append(f"            - {account.get_name()}")
        users_loop = '\n'.join(users_loop)
        return f"Infos about the bank '{self.name}':\n    Name: {self.name}\n    Users & accounts:\n{users_loop}\n    Assets: {sum(account.get_balance() for account in self.accounts):.2f}€\n"

    def get_name(self) -> str:
        return self.name

    def create_bank_account(self, name: str, initAmount: float, owner: User) -> BankAccount:
        account = BankAccount(self, name, initAmount, owner)
        owner.add_bank_account(account)
        self.accounts.append(account)
        return account
    
    def get_accounts_from_user(self, user: User) -> list[BankAccount]:
        return [account for account in self.accounts if account.owner == user]

banqueDeFrance = Bank("Banque de France")
bankOfAmerica = Bank("Bank of America")

antoine = User("Antoine", "Arnoux")
john = User("John", "Doe")

livretA = banqueDeFrance.create_bank_account("livret A", 1000, antoine)
livretB = banqueDeFrance.create_bank_account("livret B", 1000, antoine)
foreignAccount = bankOfAmerica.create_bank_account("foreign account", 500, antoine)
livretEpargne = banqueDeFrance.create_bank_account("livret épargne", 1000, john)
checkingAccount = bankOfAmerica.create_bank_account("checking account", 700, john)

print(banqueDeFrance)
print(bankOfAmerica)

foreignAccount.deposit(15)
foreignAccount.withdraw(1)
foreignAccount.transfert(50, livretEpargne)
for transaction in foreignAccount.get_transactions():
    print(transaction)

print(livretEpargne)

print(antoine)
print(john)
