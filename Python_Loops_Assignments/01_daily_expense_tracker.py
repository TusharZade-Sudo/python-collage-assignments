# Mini Project 1: Daily Expense Tracker

days = int(input("Enter number of days: "))

if days <= 0:
    print("Invalid number of days")
else:
    total = 0.0
    highest = 0.0

    for day in range(1, days + 1):
        expense = float(input(f"Enter expense for day {day}: "))
        while expense < 0:
            print("Expense cannot be negative.")
            expense = float(input(f"Enter expense for day {day} again: "))

        total += expense
        if day == 1 or expense > highest:
            highest = expense

    print(f"Total Expense: ₹{total:.2f}")
    print(f"Average Daily Expense: ₹{total / days:.2f}")
    print(f"Highest Daily Expense: ₹{highest:.2f}")
    print("Budget Alert" if total > 5000 else "Budget Within Limit")
