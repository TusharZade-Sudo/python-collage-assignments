balance = 5000.0
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("Balance:", balance)
    case 2:
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print("Updated balance:", balance)
        else:
            print("Invalid amount")
    case 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount")
        elif amount <= balance:
            balance -= amount
            print("Updated balance:", balance)
        else:
            print("Insufficient balance")
    case _:
        print("Invalid choice")
