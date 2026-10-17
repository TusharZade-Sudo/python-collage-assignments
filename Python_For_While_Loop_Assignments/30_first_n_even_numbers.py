# 30. Generate first n even numbers
n = int(input("Enter n: "))
for i in range(1, max(0, n) + 1):
    print(i * 2)
