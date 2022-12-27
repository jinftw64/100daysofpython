# 100 Days of Python
# Day 05 - Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_total = nr_letters + nr_symbols + nr_numbers

password = ""

for char in range(nr_total):
    nested_list = []
    if nr_letters > 0:
        nested_list.append(letters)
    if nr_symbols > 0:
        nested_list.append(symbols)
    if nr_numbers > 0:
        nested_list.append(numbers)
    random_list = random.choice(nested_list)
    password += random.choice(random_list)
    if random_list == letters:
        nr_letters -= 1
    elif random_list == symbols:
        nr_symbols -= 1
    elif random_list == numbers:
        nr_numbers -= 1

print(password)
