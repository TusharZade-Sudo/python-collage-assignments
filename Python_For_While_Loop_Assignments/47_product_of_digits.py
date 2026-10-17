# 47. Find product of digits of a number
n = abs(int(input("Enter an integer: ")))
product = 0 if n == 0 else 1
while n > 0:
    product *= n % 10
    n //= 10
print("Product of digits =", product)
