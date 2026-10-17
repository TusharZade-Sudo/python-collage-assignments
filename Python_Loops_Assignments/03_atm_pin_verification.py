# Mini Project 3: ATM PIN Verification

correct_pin = "1234"  # Sample PIN for this assignment
attempts = 0
access_granted = False

while attempts < 3:
    entered_pin = input("Enter your ATM PIN: ")
    attempts += 1

    if entered_pin == correct_pin:
        print("Access Granted")
        access_granted = True
        break
    else:
        print("Incorrect PIN")

print(f"Attempts Used: {attempts}")
if not access_granted:
    print("Card Temporarily Locked")
