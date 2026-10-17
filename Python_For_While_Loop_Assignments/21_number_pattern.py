# 21. Print a pattern of numbers
rows = int(input("Enter number of rows: "))
for i in range(1, max(0, rows) + 1):
    print(" ".join(str(j) for j in range(1, i + 1)))
