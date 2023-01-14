# 100 Days of Code
# Day 7
from random import choice
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = choice(word_list)
word_length = len(chosen_word)
display = []
lives = 6
end_of_game = False

stages = hangman_art.stages
logo = hangman_art.logo
print(logo)

for letter in range(word_length):
    display.append("_")

while not end_of_game:
    print(f"{' '.join(display)}")
    print(stages[lives])
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose.")
            print(f"The word was {chosen_word}.")
            end_of_game = True

    if "_" not in display:
        print("You win!")
        end_of_game = True
