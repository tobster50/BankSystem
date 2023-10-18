class Account:
    def __init__ (self, accountName, accountType, accountPassword, accountBalance):
        self.accountName = accountName
        self.accountType = accountType
        self.accountPassword = accountPassword
        self.accountBalance = accountBalance

    def deposit(self):
        print(f"Current balance: {self.accountBalance}")
        deposit = input("How much would you like to deposit? ")
        deposit = int(deposit)
        self.accountBalance += deposit
        print(f"You have deposited £{deposit}!")

    def withdraw(self):
        print(f"\nCurrent Balance: {self.accountBalance}")
        if self.accountBalance <= 0:
            print(f"\nYou cannot withdraw because you have no money!")
        else:
            withdraw = input("\nHow much would you like to deposit? ")
            withdraw = int(withdraw)
            print(f"\nYou have withdrawn £{withdraw}!")
            self.accountBalance - withdraw
    
    def modify(self):
        modify = 1
        while modify == 1:
            print("What would you like to modify?")
            print("1. Account Holder Name")
            print("2. Account Type")
            print("3. Account Password")
            choice = input("\nInput your choice 1-3")
            choice = int(choice)
            if choice == 1:
                print(f"\nYour current name is: {self.accountName}")
                name = input("What would you like to change this to? ")
                self.accountName = name
                modify = 0
            elif choice == 2:
                print(f"Your current account type is: {self.accountType}")
                if self.accountType == "Credit":
                    print("Would you like to switch to a Savings account?")
                    choice = input("Y/N: ")
                    if choice == "y" or choice == "Y":
                        self.accountType = "Savings"
                        print("Your account is now a Savings account")
                        modify = 0
                    else:
                        print("Try again")
                elif self.accountType == "Savings":
                    print("Would you like to switch to a Credit account?")
                    choice = input("Y/N: ")
                    if choice == "y" or choice == "Y":
                        self.accountType = "Credit"
                        print("Your account is now a Credit account")
                        modify = 0
                    else:
                        print("Try again")
            elif choice == 3:
                password = input("Please input your current password: ")
                if password == self.accountPassword:
                    print("Password match")
                    newPassword = input("Please input your new password: ")
                    self.accountPassword = newPassword
                    modify = 0
                else:
                    print("Password does not match")
            else:
                print("Try again.")

    def accountDetail (self):
        print(f"ACCOUNT HOLDER NAME: {self.accountName}")
        print(f"ACCOUNT TYPE: {self.accountType}")
        print(f"CURRENT BALANCE: £{self.accountBalance}")


       
