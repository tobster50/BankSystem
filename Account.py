class Account:
    def __init__ (self, accountName, accountType, accountPassword, accountBalance):
        self.accountName = accountName
        self.accountType = accountType
        self.accountPassword = accountPassword
        self.accountBalance = accountBalance

    def deposit(self, balance):
        print(f"Current balance: {balance}")
        deposit = input("How much would you like to deposit? ")
        deposit = int(deposit)
        balance = balance + deposit
        print(f"You have deposited £{deposit}!")
        return balance

    def withdraw(self, balance):
        print(f"\nCurrent Balance: {balance}")
        if balance <= 0:
            print(f"\nYou cannot withdraw because you have no money!")
        else:
            withdraw = input("\nHow much would you like to deposit? ")
            withdraw = int(withdraw)
            print(f"\nYou have withdrawn £{withdraw}!")
            balance = balance - withdraw
            return balance

    def accountDetail (self):
        print(f"ACCOUNT HOLDER NAME: {self.accountName}")
        print(f"ACCOUNT TYPE: {self.accountType}")
        print(f"CURRENT BALANCE: £{self.accountBalance}")


       
