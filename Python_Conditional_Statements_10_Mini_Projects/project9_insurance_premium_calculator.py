# Mini Project 9: Insurance Premium Calculator

name = input("Enter customer name: ")
age = int(input("Enter age: "))
risk = input("Enter occupation risk (Low/Medium/High): ").strip().lower()
smoker = input("Are you a smoker? (Yes/No): ").strip().lower()

if age < 0:
    print("Invalid age!")
elif risk not in ("low", "medium", "high"):
    print("Invalid occupation risk!")
elif smoker not in ("yes", "no"):
    print("Invalid smoking status!")
elif age < 18:
    print("\nCustomer Name:", name)
    print("Eligibility: Not Eligible (Age below 18)")
else:
    base_premium = 10000
    additional = 0

    if age > 50:
        additional += 5000

    if risk == "high":
        additional += 7000
    elif risk == "medium":
        additional += 3000

    if smoker == "yes":
        additional += 5000

    final_premium = base_premium + additional

    print("\n--- Insurance Premium ---")
    print("Customer Name:", name)
    print("Eligibility: Eligible")
    print("Base Premium: Rs.", base_premium)
    print("Additional Charges: Rs.", additional)
    print("Final Premium: Rs.", final_premium)

    if additional >= 10000:
        print("Risk Message: High Risk Policy")
    else:
        print("Risk Message: Normal Risk Policy")
