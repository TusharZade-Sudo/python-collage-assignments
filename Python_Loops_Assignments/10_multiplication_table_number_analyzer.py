# Mini Project 10: Multiplication Table and Number Analyzer

number = int(input("Enter a positive integer for the multiplication table: "))

if number <= 0:
    print("Invalid number. Enter a positive integer.")
else:
    print(f"\nMultiplication Table of {number}")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

start = int(input("\nEnter range start: "))
end = int(input("Enter range end: "))

if start > end:
    print("Invalid range: start cannot be greater than end.")
else:
    even_count = 0
    odd_count = 0
    total = 0

    for value in range(start, end + 1):
        total += value
        if value % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"Even Count: {even_count}")
    print(f"Odd Count: {odd_count}")
    print(f"Sum of Range: {total}")
