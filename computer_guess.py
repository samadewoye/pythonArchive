
import random


secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("make a guess between 1 and 10 : "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations. You win!")
        break
    elif guess < secret_number:
        if guess_count == guess_limit:
            guess_count += 1
            print("you cannot guess again")
            break

        else:
            print("Sorry,Guess again. Too low")

    elif guess > secret_number:
        if guess_count == guess_limit:
            guess_count += 1
            print("you cannot guess again")
            break

        else:
            print("Sorry,Guess again. Too High")


# print(f"Sorry, You could not guess the right number in {guess_limit} trials")
# else:
#     print("Sorry. You Failed!")
