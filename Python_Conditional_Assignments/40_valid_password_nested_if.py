password = input("Enter password: ")
if len(password) >= 8:
    if any(ch.isdigit() for ch in password):
        print("Valid password")
    else:
        print("Password must contain a digit")
else:
    print("Password must contain at least 8 characters")
