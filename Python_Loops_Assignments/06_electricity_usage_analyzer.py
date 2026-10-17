# Mini Project 6: Electricity Usage Analyzer

days = int(input("Enter number of days: "))

if days <= 0:
    print("Invalid number of days.")
else:
    total_units = 0.0
    high_usage_days = 0
    maximum_usage = 0.0

    for day in range(1, days + 1):
        units = float(input(f"Enter electricity units for day {day}: "))
        while units < 0:
            print("Units cannot be negative.")
            units = float(input(f"Enter units for day {day} again: "))

        total_units += units
        if units > 10:
            high_usage_days += 1
        if day == 1 or units > maximum_usage:
            maximum_usage = units

    print(f"Total Units: {total_units:.2f}")
    print(f"Average Daily Usage: {total_units / days:.2f}")
    print(f"High-Usage Days: {high_usage_days}")
    print(f"Maximum Daily Usage: {maximum_usage:.2f}")
    print("High Usage" if total_units > 300 else "Normal Usage")
