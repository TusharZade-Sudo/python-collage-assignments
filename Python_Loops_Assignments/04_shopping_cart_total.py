# Mini Project 4: Shopping Cart Total

n = int(input("Enter number of products: "))

if n <= 0:
    print("Invalid number of products.")
else:
    subtotal = 0.0

    for i in range(1, n + 1):
        price = float(input(f"Enter price of product {i}: ₹"))
        quantity = int(input(f"Enter quantity of product {i}: "))

        while price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            price = float(input(f"Enter price of product {i} again: ₹"))
            quantity = int(input(f"Enter quantity of product {i} again: "))

        subtotal += price * quantity

    discount = subtotal * 0.10 if subtotal >= 3000 else 0.0
    discounted_amount = subtotal - discount
    delivery = 100.0 if discounted_amount < 1500 else 0.0
    final_amount = discounted_amount + delivery

    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"Delivery Charge: ₹{delivery:.2f}")
    print(f"Final Payable Amount: ₹{final_amount:.2f}")
