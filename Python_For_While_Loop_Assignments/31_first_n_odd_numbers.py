# 31. Generate first n odd numbers
n = int(input("Enter n: "))
for i in range(max(0, n)):
    print(2 * i + 1)
