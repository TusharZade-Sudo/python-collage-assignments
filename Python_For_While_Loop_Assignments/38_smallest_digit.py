# 38. Find smallest digit in a number
n = abs(int(input("Enter an integer: ")))
smallest = 0 if n == 0 else 9
while n > 0:
    smallest = min(smallest, n % 10)
    n //= 10
print("Smallest digit =", smallest)
