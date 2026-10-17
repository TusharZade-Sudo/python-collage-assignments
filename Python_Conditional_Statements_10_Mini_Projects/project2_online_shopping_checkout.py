# Mini Project 2: Online Shopping Checkout

name = input("Enter customer name: ")
amount = float(input("Enter purchase amount: Rs. "))
customer_type = input("Enter customer type (Regular/Premium): ").strip().lower()

if amount < 0:
    print("Invalid purchase amount!")
elif customer_type not in ("regular", "premium"):
    print("Invalid customer type!")
else:
    if amount >= 5000:
        rate = 0.20
    elif amount >= 3000:
        rate = 0.10
    elif amount >= 1000:
        rate = 0.05
    else:
        rate = 0

    if customer_type == "premium":
        rate += 0.05

    discount = amount * rate
    discounted_amount = amount - discount

    if discounted_amount >= 2000:
        delivery = 0
    else:
        delivery = 100

    final_amount = discounted_amount + delivery

    print("\n--- Shopping Bill ---")
    print("Customer Name:", name)
    print("Discount: Rs.", round(discount, 2))
    print("Delivery Charge: Rs.", delivery)
    print("Final Payable Amount: Rs.", round(final_amount, 2))
