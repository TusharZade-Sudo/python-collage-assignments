# Mini Project 5: Number Guessing Game

secret_number = 37
attempts = 0
won = False

while attempts < 5:
    guess = int(input("Guess the secret number (1-100): "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You won.")
        won = True
        break
    elif guess < secret_number:
        print("Too low")
    else:
        print("Too high")

print(f"Attempts Used: {attempts}")
if not won:
    print(f"You lose! The secret number was {secret_number}.")
