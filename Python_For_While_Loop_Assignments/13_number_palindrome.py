# 13. Check whether a number is a palindrome
n = int(input("Enter an integer: "))
original = n
num = abs(n)
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
if n >= 0 and original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
