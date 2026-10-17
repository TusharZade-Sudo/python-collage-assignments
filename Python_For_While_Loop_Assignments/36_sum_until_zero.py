# 36. Find sum of numbers entered until 0 is entered
total = 0
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    total += n
print("Sum =", total)
