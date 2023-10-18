from datetime import datetime

class BalanceException(Exception):
    def __init__(self, message="La balance n'est pas suffisante."):
        self.message = message
        super().__init__(self.message)

class User:
    def __init__(self, first_name: str, last_name: str, dob: datetime):
        self.first_name = first_name
        self.last_name = last_name
        self.name = f"{first_name} {last_name}"
        self.dob = dob
        self.bank_accounts = []
    
    def __str__(self) -> str:
        return f"Prénom : {self.first_name}, Nom : {self.last_name}, Anniversaire : {self.dob}, Comptes en banque : {self.bank_accounts}"

    def get_first_name(self) -> str:
        return self.first_name
    
    def set_last_name(self, name: str) -> None:
        self.last_name = name

    def get_name(self) -> str:
        return self.name

class BankAccount:
    def __init__(self, name: str, init_balance: float, owner: User, bank: "Bank"):
        self.name = name
        self.balance = init_balance
        self.owner = owner
        self.bank = bank

    def __str__(self) -> str:
        return f"Compte banquaire '{self.name}' de '{self.bank}' appartenant à '{self.owner.get_name()}' ayant pour état {self.balance:.2f}€"

    def get_name(self) -> str:
        return self.name

    def get_balance(self) -> float:
        return self.balance
    
    def deposit(self, amount: float) -> None:
        self.balance += amount

    def is_balance_sufficient(self, amount: float, type: str = "") -> None:
        if amount > self.balance:
            message = ""
            match type:
                case "withdraw":
                    message = "Balance non suffisante pour un retrait."
                case "transfer":
                    message = "Balance non suffisante pour un transfer."
                case "":
                    message = ""
                case _:
                    message = ""
            raise BalanceException(message) if message else BalanceException

    def withdraw(self, amount: float) -> None:
        try:
            self.is_balance_sufficient(amount, "withdraw")
            self.balance -= amount
            print(f"Retrait de {amount:.2f}€ effectué")
        except BalanceException as error:
            print(f"Retrait de {amount:.2f}€ impossible : {error}")

    def transfer(self, amount: float, compte_destinataire: "BankAccount") -> None:
        try:
            self.is_balance_sufficient(amount, "transfer")
            self.balance -= amount
            compte_destinataire.deposit(amount)
            print(f"Transfer de '{self.name}' vers '{compte_destinataire.get_name()}' pour un montant de {amount:.2f}€ effectué.")
        except BalanceException as error:
            print(f"Transfer de '{self.name}' vers '{compte_destinataire.get_name()}' pour un montant de {amount:.2f}€ impossible : {error}")

class Bank():
    def __init__(self, name: str):
        self.name = name
        self.bank_accounts: list[BankAccount] = []

    def __str__(self) -> str:
        string = f"Comptes géré par la banque '{self.name}'\n"
        for bank_account in self.bank_accounts:
            string += f"    - {bank_account.get_name()}\n"
        return string

    def get_name(self) -> str:
        return self.name

    def create_bank_account(self, name: str, init_balance: float, owner: User) -> BankAccount:
        compte = BankAccount(name, init_balance, owner, self)
        self.bank_accounts.append(compte)
        return compte

antoine = User("antoine", "arnoux", datetime(2002, 6, 11))
christian = User("christian", "schaal", datetime(1957, 3, 14))
banque = Bank("CMDP")
toto = banque.create_bank_account("toto", 1000, antoine)
titi = banque.create_bank_account("titi", 1000, christian)

print(banque)