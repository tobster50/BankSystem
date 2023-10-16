from Bank import *
from Account import *

bank = Bank("Lloyds")

print("**********************")
print("BANK MANAGEMENT SYSTEM")
print("**********************")

input("ENTER to continue:")

login = 0
while login == 0:
    print(f"\nWelcome to {bank.bankName}!")
    print("1. Log in")
    print("2. Create Account")
    choice = input("Select your Option (1-2) ")
    choice = int(choice)
    if choice == 1:
        bank.accessAccount()
    elif choice == 2:
        bank.openAccount()
    elif choice == 5:
        bank.showAccounts()

active = 0
while active == 0:

    print(" 1. NEW ACCOUNT")
    print(" 2. DEPOSIT AMOUNT")
    print(" 3. WITHDRAW AMOUNT")
    print(" 4. BALANCE ENQUIRY")
    print(" 5. ALL ACCOUNT HOLDER LIST")
    print(" 6. CLOSE AN ACCOUNT")
    print(" 7. MODIFY AN ACCOUNT")
    print(" 8. EXIT")

    choice = input(" Select your Option (1-8) ")
    choice = int(choice)
    if choice == 1:
        bank.openAccount()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        bank.showAccounts()
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        pass
