import sys
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
    elif choice == 3:
        sys.exit()
    elif choice == 5:
        bank.showAccounts()

"""
1. NEW ACCOUNT
2. DEPOSIT AMOUNT
3. WITHDRAW AMOUNT
4. BALANCE ENQUIRY
5. ALL ACCOUNT HOLDER LIST
6. CLOSE AN ACCOUNT
7. MODIFY AN ACCOUNT
"""
