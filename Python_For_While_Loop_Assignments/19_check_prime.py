# 19. Check whether a number is prime
n = int(input("Enter an integer: "))
prime = n >= 2
for i in range(2, int(max(0, n) ** 0.5) + 1):
    if n % i == 0:
        prime = False
        break
print("Prime number" if prime else "Not a prime number")
