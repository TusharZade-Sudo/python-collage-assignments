# 17. Find largest digit in a number
n = abs(int(input("Enter an integer: ")))
largest = 0
while n > 0:
    largest = max(largest, n % 10)
    n //= 10
print("Largest digit =", largest)
