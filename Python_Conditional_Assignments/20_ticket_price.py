age = int(input("Enter age: "))
# Assumed prices: under 5 free, 5-17 Rs. 50, 18-59 Rs. 100, 60+ Rs. 60.
if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket price: Free")
elif age < 18:
    print("Ticket price: Rs. 50")
elif age < 60:
    print("Ticket price: Rs. 100")
else:
    print("Ticket price: Rs. 60")
