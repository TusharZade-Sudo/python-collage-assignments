# 20. Print a triangle of stars
rows = int(input("Enter number of rows: "))
for i in range(1, max(0, rows) + 1):
    print("*" * i)
