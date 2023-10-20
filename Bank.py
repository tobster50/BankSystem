from Account import *

class Bank:
    def __init__ (self, bankName):
        self.bankName = bankName
        self.allAccounts = {}
        self.accountNumber = 0

    def createAccount(self, accountName, accountType, accountPassword, accountBalance):
        newAccount = Account(accountName, accountType, accountPassword, accountBalance)
        newAccountNumber = self.accountNumber
        self.allAccounts[newAccountNumber] = newAccount
        print(f"\nACCOUNT NUMBER: {self.accountNumber}")
        #increment ready for next account creation
        self.accountNumber = self.accountNumber + 1
        Account.accountDetail(newAccount)

    def openAccount(self):
        print("\nThank you for choosing our bank!")
        print("We will require some information from you to begin: ")
        accountName = input("Name: ")
        password = 1
        while password == 1:
            accountPassword = input("Set your password: ")
            passwordCheck = input("Re-enter your password: ")
            if accountPassword == passwordCheck:
                print("Password match")
                password = 0
            else:
                print("Passwords do not match. Try again")
        type = 1
        while type == 1:
            accountType = input("Account Type: (C/c = Credit S/s = Savings)")
            if accountType == "S" or accountType == "s":
                accountType = "Savings"
                type = 0
            elif accountType == "C" or accountType == "c":
                accountType = "Credit"
                type = 0
            else:
                print("Try again")
        startingBalance = input("Input your starting account Balance: £")
        startingBalance = int(startingBalance)
        self.createAccount(accountName, accountType, accountPassword, startingBalance)
        print("Account created!")

    def passwordCheck (self, accountNumber, accountPassword):
        user = self.allAccounts[accountNumber]
        if accountPassword == user.accountPassword:
            print("Password Match")
            return 1
        else:
            print("Password doesn't match")
    
    def userInterface(self, accountNumber):
        user = self.allAccounts[accountNumber]
        session = 1
        while session == 1:
            print(f"\nWelcome back {user.accountName}! What would you like to do today?")
            print(f"\nAccount Type: {user.accountType}")
            print(f"Current Balance: £{user.accountBalance}")
            print("\n1. Withdraw")
            print("2. Deposit")
            print("3. Modify Account")
            print("5. Exit")
            choice = input("\nInput your choice 1-5")
            choice = int(choice)
            if choice == 1:
                user.withdraw()
            if choice == 2:
                user.deposit()
            if choice == 3:
                user.modify() 
            if choice == 4:
                session = 0
    
    def accessAccount(self):
        accountNumberInput = input("\nInput your account number: ")
        accountNumberInput = int(accountNumberInput)
        passwordInput = input("Input your password: ")
        check = self.passwordCheck(accountNumberInput, passwordInput)
        if check == 1:
            self.userInterface(accountNumberInput)

    def showAccounts(self):
        print("\nList of accounts: ")
        for accountNumber in self.allAccounts:
            newAccount = self.allAccounts[accountNumber]
            print(f"Account number: {accountNumber} | Account Holder Name: {newAccount.accountName} | Account Type: {newAccount.accountType} | Balance: {newAccount.accountBalance}" )


