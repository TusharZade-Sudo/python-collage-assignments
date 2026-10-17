# 11. Count number of digits in a number
n = abs(int(input("Enter an integer: ")))
if n == 0:
    count = 1
else:
    count = 0
    while n > 0:
        count += 1
        n //= 10
print("Number of digits =", count)
