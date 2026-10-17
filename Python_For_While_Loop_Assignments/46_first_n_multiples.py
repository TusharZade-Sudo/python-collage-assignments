# 46. Print first n multiples of a number
num = int(input("Enter a number: "))
n = int(input("Enter number of multiples: "))
for i in range(1, max(0, n) + 1):
    print(num * i)
