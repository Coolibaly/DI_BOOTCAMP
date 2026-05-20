# Challenge 1: List of Multiples

print("Challenge 1: List of Multiples\n")

# Ask the user for a number
number = int(input("Enter a number: "))

# Ask the user for the desired length
length = int(input("Enter the length of the list: "))

# Create an empty list
multiples = []

# Generate multiples of the number
for i in range(1, length + 1):
    multiples.append(number * i)

# Display the result
print(multiples)



# Challenge 2: Remove Consecutive Duplicate Letters

print("\nChallenge 2: Remove Consecutive Duplicate Letters\n")
# Ask the user for a word
word = input("Enter a word: ")

# Start the new string with the first character
new_word = ""

# Loop through each character in the word
for letter in word:

    # Add the character only if it is different
    # from the last character added
    if len(new_word) == 0 or letter != new_word[-1]:
        new_word += letter

# Display the cleaned word
print("Result:", new_word)