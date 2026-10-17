ch = input("Enter a character: ").lower()
if len(ch) == 1 and ch in "aeiou":
    print("Vowel")
elif len(ch) == 1 and ch.isalpha():
    print("Consonant")
else:
    print("Invalid character")
