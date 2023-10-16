from Account import *

class Bank:
    def __init__ (self, bankName):
        self.bankName = bankName
        self.allAccounts = {}
        self.accountNumber = 0

    def createAccount(self, accountName, accountType, accountPassword):
        newAccount = Account(accountName, accountType, accountPassword)
        newAccountNumber = self.accountNumber
        self.allAccounts[newAccountNumber] = newAccount
        print(f"ACCOUNT NUMBER: {self.accountNumber}")
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
            accountType = input("Account Type: ")
            if accountType == "S" or accountType == "s":
                accountType = "Savings"
                type = 0
            elif accountType == "C" or accountType == "c":
                accountType = "Credit"
                type = 0
            else:
                print("Try again")
        self.createAccount(accountName, accountType, accountPassword)
        print("Account created!")

    def passwordCheck (self, accountNumber, accountPassword):
        
        for account in self.allAccounts:
            if account == accountNumber:
                accountNumber = str(accountNumber)
                print(f"{account} equals {accountNumber}!")
                result  = self.allAccounts[account][self.accountPassword]
                print(result)
            else:
                print("Fail")
        #if self.allAccounts[accountNumber][accountPassword] == accountPassword:
        #    print("Password matches")
        #else:
        #    print("Access denied")
    
    def accessAccount(self):
        accountNumberInput = input("\nInput your account number: ")
        accountNumberInput = int(accountNumberInput)
        passwordInput = input("Input your password: ")
        self.passwordCheck(accountNumberInput, passwordInput)

    def showAccounts(self):
        print("\nList of accounts: ")
        for accountNumber in self.allAccounts:
            newAccount = self.allAccounts[accountNumber]
            print(f"Account number: {accountNumber} | Account Holder Name: {newAccount.accountName} | Account Type: {newAccount.accountType}" )


