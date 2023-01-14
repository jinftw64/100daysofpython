# 100 Days of Code
# Day 7
from random import choice
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = choice(word_list)
guessed_words = set()
word_length = len(chosen_word)
display = []
lives = 6
end_of_game = False

print(logo)

for letter in range(word_length):
    display.append("_")

while not end_of_game:
    print(f"{' '.join(display)}")
    print(stages[lives])

    guess = input("Guess a letter: ").lower()
    if guess in guessed_words:
        print(f"'{guess}' - You've already guessed this letter.")
    else:
        guessed_words.add(guess)

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"'{guess}' - This letter isn't in the word")
        lives -= 1
        if lives == 0:
            print("You lose.")
            print(f"The word was {chosen_word}.")
            end_of_game = True

    if "_" not in display:
        print("You win!")
        end_of_game = True
