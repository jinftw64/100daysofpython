# Day 02 of 100 Days of Python

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

tip_percent = int(input("What tip percent would you like to give? 10, 12 or 15? "))

num_people = int(input("How many people to split the bill? "))

personal_total = round(((bill * (1 + tip_percent / 100)) / num_people),2)

print(f"Each person should pay: {personal_total}")
