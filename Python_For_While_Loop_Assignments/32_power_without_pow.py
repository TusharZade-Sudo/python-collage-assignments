# 32. Calculate power without using pow()
base = float(input("Enter base: "))
exponent = int(input("Enter integer exponent: "))
result = 1
for _ in range(abs(exponent)):
    result *= base
if exponent < 0:
    if base == 0:
        print("Zero cannot be raised to a negative exponent.")
    else:
        result = 1 / result
        print("Power =", result)
else:
    print("Power =", result)
