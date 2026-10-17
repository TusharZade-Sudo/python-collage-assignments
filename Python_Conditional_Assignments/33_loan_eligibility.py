age = int(input("Enter age: "))
salary = float(input("Enter monthly salary: "))
# Illustrative criteria only: age >= 21 and monthly salary >= Rs. 25000.
if age >= 21:
    if salary >= 25000:
        print("Eligible to apply for loan")
    else:
        print("Salary is too low")
else:
    print("Age requirement not met")
