# def acronym_generator(string_input):
#     acronym = ""
#     if len(string_input) <= 1:
#         acronym = "There is no acronym"
#     else:
#         my_split = string_input.split()
#         for x in range(len(my_split)):
#             acronym += my_split[x][0].upper()
#     return acronym
#
#
# print(acronym_generator("yes"))
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.savings_account = BankAccount(0.6, 0)
        self.checking_account = BankAccount(0.2, 0)

    def make_deposit(self, amount, account):
        if account == 1:
            self.savings_account.deposit(amount)
        else:
            self.checking_account.deposit(amount)
        return self

    def make_withdraw(self, amount, account):
        if account == 1:
            self.savings_account.withdraw(amount)
        else:
            self.savings_account.withdraw(amount)
        return self

    def display_user_balance(self, account):
        if account == 1:
            print(f"{self.name}, your savings account balance is:{self.savings_account.balance}")
        else:
            print(f"{self.name}, your checking account balance is: {self.checking_account.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.checking_account.balance -= amount
        other_user.checking_account.balance += amount
        return self


class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def yield_interest(self):
        if self.balance > 1:
            self.balance = self.balance + (self.balance * self.int_rate)


robin = User("Robin", "robin@email")
robin.make_deposit(1400, 2).display_user_balance(2)

brady = User("Brady", "brady@email")
brady.make_deposit(2000, 2).display_user_balance(2)

brady.transfer_money(robin, 800)
brady.display_user_balance(2)

robin.display_user_balance(2)
