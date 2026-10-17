username = input("Enter username: ")
password = input("Enter password: ")
# Demo credentials only; do not use this pattern for real authentication.
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")
