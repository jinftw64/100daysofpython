# 100 Days of Code
# Day 7
from random import choice

word_list = ["ardvark", "baboon", "camel"]
chosen_word = choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
