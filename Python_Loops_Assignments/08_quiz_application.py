# Mini Project 8: Quiz Application

questions = [
    ("What is the capital of India? ", "delhi"),
    ("What is 5 + 5? ", "10"),
    ("Which programming language are you learning? ", "python"),
    ("How many days are in a week? ", "7"),
    ("What is 10 * 2? ", "20"),
]

score = 0

for question, correct_answer in questions:
    answer = input(question).strip().lower()
    if answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. Correct answer: {correct_answer}")

percentage = (score / len(questions)) * 100
print(f"\nScore: {score}/{len(questions)}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Excellent")
elif percentage >= 60:
    print("Good")
else:
    print("Keep Practicing")
