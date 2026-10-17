# Mini Project 4: Student Scholarship Eligibility

name = input("Enter student name: ")
percentage = float(input("Enter percentage: "))
income = float(input("Enter annual family income: Rs. "))
attendance = float(input("Enter attendance percentage: "))

if not (0 <= percentage <= 100 and income >= 0
        and 0 <= attendance <= 100):
    print("Invalid input!")
elif percentage >= 75 and income <= 400000 and attendance >= 75:
    print("\nStudent Name:", name)
    print("Eligibility Status: Eligible")

    if percentage >= 90:
        print("Scholarship Category: Full Scholarship")
    else:
        print("Scholarship Category: Partial Scholarship")
else:
    print("\nStudent Name:", name)
    print("Eligibility Status: Not Eligible")
    print("Reason:")

    if percentage < 75:
        print("- Percentage is below 75%.")
    if income > 400000:
        print("- Family income exceeds Rs. 400000.")
    if attendance < 75:
        print("- Attendance is below 75%.")
