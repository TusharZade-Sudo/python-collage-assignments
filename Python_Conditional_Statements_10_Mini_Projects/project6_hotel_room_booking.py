# Mini Project 6: Hotel Room Booking System

name = input("Enter guest name: ")
room_type = input("Enter room type (Standard/Deluxe/Suite): ").strip().lower()
nights = int(input("Enter number of nights: "))

if nights <= 0:
    print("Invalid number of nights!")
else:
    if room_type == "standard":
        price = 2000
    elif room_type == "deluxe":
        price = 3500
    elif room_type == "suite":
        price = 6000
    else:
        price = 0
        print("Invalid room type!")

    if price > 0:
        room_charge = price * nights

        if nights >= 10:
            discount_rate = 20
        elif nights >= 5:
            discount_rate = 10
        else:
            discount_rate = 0

        discount = room_charge * discount_rate / 100
        final_amount = room_charge - discount

        print("\n--- Hotel Booking ---")
        print("Guest Name:", name)
        print("Room Type:", room_type.title())
        print("Number of Nights:", nights)
        print("Room Charge: Rs.", round(room_charge, 2))
        print("Discount: Rs.", round(discount, 2))
        print("Final Booking Amount: Rs.", round(final_amount, 2))
