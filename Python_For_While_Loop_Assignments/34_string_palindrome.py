# 34. Check whether a string is a palindrome (ignores case and spaces)
s = input("Enter a string: ")
cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
print("Palindrome" if cleaned == cleaned[::-1] else "Not Palindrome")
