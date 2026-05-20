# Exercise 1: Hello World -------------------------------------------------

print("Exercise 1: Hello World\n")

# Print "Hello world" four times using one line of code
print("Hello world\nHello world\nHello world\nHello world")


# Exercise 2: Some Math -------------------------------------------------

print("Exercise 2: Some Math\n")

# Calculate (99^3) * 8
# In Python, ** means "power"

result = (99 ** 3) * 8

# Print the result
print(result)


# Exercise 3: What is the output? ----------------------------------

print("Exercise 3: What is the output?\n")

# Guess: False
print(15 < 8)

# Guess: False
print(5 < 3)

# Guess: True
print(3 == 3)

# Guess: False
print(3 == "3")

# Guess: Error because Python cannot compare string and integer
# print("3" > 3)

# Guess: False
print("Hello" == "hello")


# Exercise 4: Your computer brand ---------------------------------------------

print("Exercise 4: Your computer brand\n")

# Create a variable with your computer brand
computer_brand = "HP"

# Print a sentence using the variable
print("I have a", computer_brand, "computer.")


# Exercise 5: Your information ------------------------------------------------------------

print("Exercise 5: Your information\n")

# Create variables
name = "Latif"
age = 22
shoe_size = 42

# Create a sentence using the variables
info = (
    "My name is " + name +
    ", I am " + str(age) +
    " years old and my shoe size is " + str(shoe_size) + "."
)

# Print the sentence
print(info)


# Exercise 6: A & B ---------------------------------------------

print("Exercise 6: A & B\n")

# Create two number variables
a = 20
b = 10

# Check if a is bigger than b
if a > b:
    print("Hello World")



# Exercise 7: Odd or Even ----------------------------------------------

print("Exercise 7: Odd or Even\n")
# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



# Exercise 8: What's your name? ----------------------------------------------

print("Exercise 8: What's your name?\n") 

# Ask the user for their name
user_name = input("What is your name? ")

# Compare the name
if user_name == "Latif":
    print("Wow! We have the same name.")
else:
    print("Nice to meet you,", user_name + "!")



# Exercise 9: Tall enough to ride a roller coaster ----------------------------------------------

print("Exercise 9: Tall enough to ride a roller coaster\n")
# Ask the user for their height in centimeters
height = int(input("Enter your height in cm: "))

# Check if the user is tall enough
if height > 145:
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride.")