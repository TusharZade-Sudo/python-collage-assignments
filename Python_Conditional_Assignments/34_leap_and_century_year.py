year = int(input("Enter year: "))
if year <= 0:
    print("Enter a valid positive year")
else:
    if year % 100 == 0:
        print("Century year")
    else:
        print("Not a century year")
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")
