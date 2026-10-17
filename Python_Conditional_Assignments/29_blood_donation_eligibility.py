age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))
# Educational example only; actual eligibility requires local guidelines and medical screening.
if 18 <= age <= 65 and weight >= 50:
    print("Meets the basic age and weight criteria")
else:
    print("Does not meet the basic criteria")
