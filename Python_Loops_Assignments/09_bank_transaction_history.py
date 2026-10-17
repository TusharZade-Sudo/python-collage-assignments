# Mini Project 9: Bank Transaction History

balance = float(input("Enter opening balance: ₹"))
n = int(input("Enter number of transactions: "))

deposits = 0
successful_withdrawals = 0
rejected_withdrawals = 0

if balance < 0 or n < 0:
    print("Opening balance and transaction count must not be negative.")
else:
    for i in range(1, n + 1):
        print(f"\nTransaction {i}")
        transaction_type = input("Enter D for deposit or W for withdrawal: ").strip().upper()
        amount = float(input("Enter transaction amount: ₹"))

        if amount <= 0:
            print("Invalid transaction amount.")
        elif transaction_type == "D":
            balance += amount
            deposits += 1
            print("Deposit Successful")
        elif transaction_type == "W":
            if amount <= balance:
                balance -= amount
                successful_withdrawals += 1
                print("Withdrawal Successful")
            else:
                rejected_withdrawals += 1
                print("Insufficient Balance. Withdrawal Rejected.")
        else:
            print("Invalid transaction type.")

    print(f"\nFinal Balance: ₹{balance:.2f}")
    print(f"Deposit Count: {deposits}")
    print(f"Successful Withdrawal Count: {successful_withdrawals}")
    print(f"Rejected Withdrawal Count: {rejected_withdrawals}")
    if balance < 1000:
        print("Warning: Balance Below ₹1,000")
