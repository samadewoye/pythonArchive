
from random import random

import random

user = input(
    "What's your choice? r for Rock , s for Scissors and p for Paper: ")
computer = random.choice(["r", "s", "p"])
print(f"The computer choose {computer} ")

# r>s, s>p, p>r

if user == computer:
    print("It's a tie")
elif (user == "r" and computer == "s") or (user == "s" and computer == "p") \
        or (user == "p" and computer == "r"):
    print("You win!")
else:
    print("You lose!")
