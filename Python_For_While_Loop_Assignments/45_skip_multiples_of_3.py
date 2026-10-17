# 45. Print numbers skipping multiples of 3, from 1 to 50
for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)
