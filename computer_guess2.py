import random

secret_number = 5
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    computer_guess = random.randint(1, 10)
    if computer_guess != secret_number:
        print("The computer guessed  wrong, try again")
    elif computer_guess == secret_number:
        print(f"Hurray!, The computer guessed {secret_number} correctly")
        break
    else:
        print("The computer has not made any guess!")
    print(computer_guess)
    guess_count += 1
