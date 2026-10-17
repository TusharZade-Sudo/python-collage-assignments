# 18. Print prime numbers between 1 and 50
for n in range(2, 51):
    prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    if prime:
        print(n)
