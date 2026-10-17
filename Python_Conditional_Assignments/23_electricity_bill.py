units = float(input("Enter units consumed: "))
# Assumed slabs: first 100 at Rs. 1.50, next 100 at Rs. 2.50, remaining at Rs. 4.
if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 1.5
    print("Bill:", bill)
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5
    print("Bill:", bill)
else:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
    print("Bill:", bill)
