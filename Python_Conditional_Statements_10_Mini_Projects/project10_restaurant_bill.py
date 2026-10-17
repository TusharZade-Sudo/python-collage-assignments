# Mini Project 10: Restaurant Bill and Service Charge

name = input("Enter customer name: ")
bill = float(input("Enter food bill amount: Rs. "))
membership = input("Do you have membership? (Yes/No): ").strip().lower()

if bill < 0:
    print("Invalid bill amount!")
elif membership not in ("yes", "no"):
    print("Invalid membership status!")
else:
    if bill >= 5000:
        discount_rate = 15
    elif bill >= 3000:
        discount_rate = 10
    elif bill >= 1000:
        discount_rate = 5
    else:
        discount_rate = 0

    if membership == "yes":
        discount_rate += 5

    discount = bill * discount_rate / 100
    discounted_bill = bill - discount
    service_charge = discounted_bill * 0.05
    final_bill = discounted_bill + service_charge

    print("\n--- Restaurant Bill ---")
    print("Customer Name:", name)
    print("Original Bill: Rs.", round(bill, 2))
    print("Discount: Rs.", round(discount, 2))
    print("Service Charge: Rs.", round(service_charge, 2))
    print("Final Payable Amount: Rs.", round(final_bill, 2))

    if final_bill >= 5000:
        print("Thank you for being a valued customer")
    else:
        print("Thank you for visiting!")
