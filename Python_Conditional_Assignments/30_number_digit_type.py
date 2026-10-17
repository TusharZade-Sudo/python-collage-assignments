n = abs(int(input("Enter a number: ")))
if n <= 9:
    print("Single-digit number")
elif n <= 99:
    print("Double-digit number")
elif n <= 999:
    print("Three-digit number")
else:
    print("More than three digits")
