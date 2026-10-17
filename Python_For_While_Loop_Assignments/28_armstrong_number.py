# 28. Check whether a number is an Armstrong number
n = int(input("Enter a non-negative integer: "))
if n < 0:
    print("Not an Armstrong number")
else:
    digits = str(n)
    total = sum(int(digit) ** len(digits) for digit in digits)
    print("Armstrong number" if total == n else "Not an Armstrong number")
