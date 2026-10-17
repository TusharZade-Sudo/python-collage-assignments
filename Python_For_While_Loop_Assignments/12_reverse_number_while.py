# 12. Reverse a number using while loop
n = int(input("Enter an integer: "))
num = abs(n)
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
if n < 0:
    rev = -rev
print("Reversed number =", rev)
