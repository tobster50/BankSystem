class Account:
    def __init__ (self, accountName, accountType, accountPassword):
        self.accountName = accountName
        self.accountType = accountType
        self.accountPassword = accountPassword
        self.balance = 0

    def deposit(self, depositAmount):
        if depositAmount >= 0:
            return self.balance + depositAmount
        elif depositAmount < 0:
            print("You cannot deposit a negative value")

    def accountDetail (self):
        print(f"ACCOUNT HOLDER NAME: {self.accountName}")
        print(f"ACCOUNT TYPE: {self.accountType}")
        print(f"CURRENT BALANCE: £{self.balance}")


       
