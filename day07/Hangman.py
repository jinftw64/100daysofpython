# 100 Days of Code
# Day 7
from random import choice

word_list = ["ardvark", "baboon", "camel"]
chosen_word = choice(word_list)

print(f"This is the solution: {chosen_word}")
guess = input("Guess a letter: ").lower()

display = []
for letter in range(len(chosen_word)):
    display.append("_")

for position in range(len(chosen_word)):
    if chosen_word[position] == guess:
        display[position] = chosen_word[position]

print(display)
