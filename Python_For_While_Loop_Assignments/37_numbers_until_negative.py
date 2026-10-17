# 37. Print numbers until a negative number is entered
while True:
    n = int(input("Enter a number (negative to stop): "))
    if n < 0:
        break
    print(n)
