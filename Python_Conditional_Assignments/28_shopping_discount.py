amount = float(input("Enter shopping amount: "))
# Assumed discounts: 20% for Rs. 5000+, 10% for Rs. 2000+, otherwise 0%.
if amount < 0:
    print("Invalid amount")
else:
    if amount >= 5000:
        discount = amount * 0.20
    elif amount >= 2000:
        discount = amount * 0.10
    else:
        discount = 0
    print("Discount:", discount)
    print("Final amount:", amount - discount)
