# 100 Days of Code
# Day 7
from random import choice

word_list = ["ardvark", "baboon", "camel"]
chosen_word = choice(word_list)
word_length = len(chosen_word)
display = []

for letter in range(word_length):
    display.append("_")

while "_" in display:
    print(f"This is the solution: {chosen_word}")
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

print("You win!")
