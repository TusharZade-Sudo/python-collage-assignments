# 43. Calculate sum of cubes of first n numbers
n = int(input("Enter n: "))
total = 0
for i in range(1, max(0, n) + 1):
    total += i ** 3
print("Sum of cubes =", total)
