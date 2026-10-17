# 27. Print all factors of a positive integer
n = int(input("Enter a positive integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
