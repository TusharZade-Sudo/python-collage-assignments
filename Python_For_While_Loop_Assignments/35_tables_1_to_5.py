# 35. Print multiplication tables from 1 to 5
for n in range(1, 6):
    print(f"Table of {n}")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    print()
