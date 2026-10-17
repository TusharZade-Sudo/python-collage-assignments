# Mini Project 8: Movie Ticket Booking

name = input("Enter customer name: ")
age = int(input("Enter age: "))
show = input("Enter show type (Morning/Evening): ").strip().lower()
day = input("Enter day type (Weekday/Weekend): ").strip().lower()

if age < 0:
    print("Invalid age!")
elif show not in ("morning", "evening"):
    print("Invalid show type!")
elif day not in ("weekday", "weekend"):
    print("Invalid day type!")
else:
    original_price = 200

    if age < 12:
        discount = original_price * 0.50
    elif age >= 60:
        discount = original_price * 0.30
    else:
        discount = 0

    if show == "morning":
        discount += 30

    if day == "weekend":
        surcharge = 50
    else:
        surcharge = 0

    final_price = max(0, original_price - discount + surcharge)

    print("\n--- Movie Ticket ---")
    print("Customer Name:", name)
    print("Original Ticket Price: Rs.", original_price)
    print("Total Discount: Rs.", round(discount, 2))
    print("Weekend Surcharge: Rs.", surcharge)
    print("Final Ticket Price: Rs.", round(final_price, 2))
