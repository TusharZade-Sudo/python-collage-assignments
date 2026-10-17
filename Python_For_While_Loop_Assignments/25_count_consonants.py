# 25. Count consonants in a string
s = input("Enter a string: ")
count = sum(1 for ch in s.lower() if ch.isalpha() and ch not in "aeiou")
print("Consonants =", count)
