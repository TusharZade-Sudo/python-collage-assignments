marks = float(input("Enter marks: "))
# Assumed grading: Distinction >= 75, First Class >= 60, Pass >= 40, otherwise Fail.
if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
