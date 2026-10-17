# 14. Print Fibonacci series up to n terms
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(max(0, n)):
    print(a, end=" ")
    a, b = b, a + b
print()
