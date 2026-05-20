# Exercise 1: What is the Season?

print("Exercise 1: What is the Season?\n")

# Ask the user for a month number
month = int(input("Enter a month (1-12): "))

# Determine the season based on the month
if month in [3, 4, 5]:
    print("Season: Spring")
elif month in [6, 7, 8]:
    print("Season: Summer")
elif month in [9, 10, 11]:
    print("Season: Autumn")
else:
    print("Season: Winter")



# Exercise 2: For Loop

print("Exercise 2: For Loop\n")
# Print numbers from 1 to 20
for i in range(1, 21):
    print(i)

# Print numbers from 1 to 20 with even index
for i in range(1, 21):
    if i % 2 == 0:
        print(i)



# Exercise 3: While Loop

print("Exercise 3: What is the output?\n")
# Define target name (change if needed)
my_name = "Latif"

# Ask user repeatedly until they enter the correct name
user_input = ""

while user_input != my_name:
    user_input = input("Enter your name: ")


# Exercise 4: Check the index

print("Exercise 4: Check the index\n")

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask user for a name
search_name = input("Enter a name: ")

# Check if name exists in list
if search_name in names:
    print("Index of first occurrence:", names.index(search_name))
else:
    print("Name not found")


# Exercise 5: Greatest Number

print("Exercise 5: Greatest Number\n")

# Ask user for three numbers
num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))
num3 = int(input("Input the 3rd number: "))

# Determine the greatest number
greatest = num1

if num2 > greatest:
    greatest = num2

if num3 > greatest:
    greatest = num3

# Print result
print("The greatest number is:", greatest)


# =========================================================
# Exercise 6: Random number game
# =========================================================

import random

wins = 0
losses = 0

while True:
    # Ask user for guess
    guess = input("Guess a number from 1 to 9 (or type quit): ")

    # Exit condition
    if guess.lower() == "quit":
        break

    guess = int(guess)

    # Generate random number
    secret = random.randint(1, 9)

    # Compare
    if guess == secret:
        print("Winner")
        wins += 1
    else:
        print("Better luck next time.")
        losses += 1

# Show final score
print("Game Over")
print("Wins:", wins)
print("Losses:", losses)