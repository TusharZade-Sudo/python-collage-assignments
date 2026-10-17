# 24. Count vowels in a string
s = input("Enter a string: ")
count = sum(1 for ch in s.lower() if ch in "aeiou")
print("Vowels =", count)
