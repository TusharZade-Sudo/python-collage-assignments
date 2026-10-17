# 23. Find sum of odd digits in a number
n = abs(int(input("Enter an integer: ")))
total = 0
while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        total += digit
    n //= 10
print("Sum of odd digits =", total)
