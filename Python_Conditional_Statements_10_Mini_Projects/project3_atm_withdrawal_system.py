# Mini Project 3: ATM Withdrawal System

name = input("Enter account holder name: ")
balance = float(input("Enter current balance: Rs. "))
withdraw = float(input("Enter withdrawal amount: Rs. "))

if balance < 0:
    print("Invalid account balance!")
elif withdraw <= 0:
    print("Transaction Rejected: Amount must be greater than zero.")
elif withdraw > balance:
    print("Transaction Rejected: Insufficient balance.")
elif withdraw > 20000:
    print("Transaction Rejected: Maximum limit is Rs. 20000.")
else:
    remaining = balance - withdraw

    print("\n--- ATM Transaction ---")
    print("Account Holder:", name)
    print("Transaction Status: Successful")
    print("Withdrawn Amount: Rs.", round(withdraw, 2))
    print("Remaining Balance: Rs.", round(remaining, 2))

    if remaining < 1000:
        print("Low Balance Warning")
