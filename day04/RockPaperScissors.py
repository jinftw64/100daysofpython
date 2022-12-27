# 100 Days of Python

from random import choice

victory = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
        }

moves = ["rock", "paper", "scissors"]

player_move = input("What do you choose? Rock, Paper, or Scissors? ")

computer_move = choice(moves)

print(f"You chose: {player_move}")
print(f"Computer chose: {computer_move}")

if computer_move.lower() == player_move.lower():
    print("Tie!")
elif computer_move == victory[player_move.lower()]:
    print("You win!")
else:
    print("You lose!")
