# 48. Check whether a number is a Strong number
n = int(input("Enter a non-negative integer: "))
original = n
total = 0
if n >= 0:
    if n == 0:
        total = 1  # 0! = 1
    while n > 0:
        digit = n % 10
        fact = 1
        for i in range(1, digit + 1):
            fact *= i
        total += fact
        n //= 10
    print("Strong number" if total == original else "Not a Strong number")
else:
    print("Not a Strong number")
