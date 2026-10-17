# Mini Project 7: Employee Payroll Summary

n = int(input("Enter number of employees: "))

if n <= 0:
    print("Invalid number of employees.")
else:
    total_net_payroll = 0.0

    for i in range(1, n + 1):
        name = input(f"Enter name of employee {i}: ")
        basic_salary = float(input("Enter basic salary: ₹"))
        overtime_hours = float(input("Enter overtime hours: "))

        while basic_salary < 0 or overtime_hours < 0:
            print("Salary and overtime hours cannot be negative.")
            basic_salary = float(input("Enter basic salary again: ₹"))
            overtime_hours = float(input("Enter overtime hours again: "))

        overtime_pay = overtime_hours * 200
        gross_salary = basic_salary + overtime_pay
        deduction_rate = 0.10 if gross_salary >= 50000 else 0.05
        deduction = gross_salary * deduction_rate
        net_salary = gross_salary - deduction
        total_net_payroll += net_salary

        print(f"\nEmployee: {name}")
        print(f"Gross Salary: ₹{gross_salary:.2f}")
        print(f"Deduction: ₹{deduction:.2f}")
        print(f"Net Salary: ₹{net_salary:.2f}")

    print(f"\nEmployee Count: {n}")
    print(f"Total Net Payroll: ₹{total_net_payroll:.2f}")
