# Mini Project 5: Employee Performance Bonus

name = input("Enter employee name: ")
salary = float(input("Enter monthly salary: Rs. "))
experience = float(input("Enter years of experience: "))
rating = int(input("Enter performance rating (1-5): "))

if salary < 0 or experience < 0:
    print("Invalid salary or experience!")
elif rating < 1 or rating > 5:
    print("Invalid rating! Enter a value from 1 to 5.")
else:
    if experience >= 10 and rating >= 4:
        bonus_rate = 20
    elif experience >= 5 and rating >= 4:
        bonus_rate = 15
    elif experience >= 2 and rating >= 3:
        bonus_rate = 10
    else:
        bonus_rate = 0

    bonus = salary * bonus_rate / 100
    final_salary = salary + bonus

    print("\n--- Employee Bonus ---")
    print("Employee Name:", name)
    print("Bonus Percentage:", bonus_rate, "%")
    print("Bonus Amount: Rs.", round(bonus, 2))
    print("Final Salary: Rs.", round(final_salary, 2))

    if rating == 5:
        print("Performance Message: Excellent Performer")
    elif bonus_rate > 0:
        print("Performance Message: Good Performer")
    else:
        print("Performance Message: No Bonus")
