print("1. English")
print("2. Hindi")
print("3. Marathi")
choice = int(input("Select language: "))
match choice:
    case 1:
        print("English selected")
    case 2:
        print("Hindi selected")
    case 3:
        print("Marathi selected")
    case _:
        print("Invalid choice")
