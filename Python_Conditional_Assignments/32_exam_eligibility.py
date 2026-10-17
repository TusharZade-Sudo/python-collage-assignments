attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks: "))
# Assumed requirements: attendance >= 75% and marks >= 40.
if attendance >= 75:
    if marks >= 40:
        print("Eligible for exam")
    else:
        print("Not eligible: Low marks")
else:
    print("Not eligible: Low attendance")
