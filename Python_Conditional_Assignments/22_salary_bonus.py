salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))
# Assumed bonus: 10% for 5 or more years of service.
if years >= 5:
    bonus = salary * 0.10
    print("Bonus:", bonus)
else:
    print("No bonus")
