# 22. Find sum of even digits in a number
n = abs(int(input("Enter an integer: ")))
total = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        total += digit
    n //= 10
print("Sum of even digits =", total)
