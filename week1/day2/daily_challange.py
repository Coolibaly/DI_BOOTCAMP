
# Challenge 1: Letter Index Dictionary


# Ask the user for a word
word = input("Enter a word: ")

# Create an empty dictionary
letter_indexes = {}

# Loop through each character with its index
for index, letter in enumerate(word):

    # Check if the letter already exists in the dictionary
    if letter in letter_indexes:

        # Add the index to the existing list
        letter_indexes[letter].append(index)

    else:
        # Create a new key with a list containing the index
        letter_indexes[letter] = [index]

# Display the dictionary
print(letter_indexes)



# Challenge 2: Affordable Items


# Dictionary of items and prices
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

# Wallet amount
wallet = "$300"

# Remove dollar sign and commas from wallet
wallet = wallet.replace("$", "").replace(",", "")

# Convert wallet to integer
wallet_amount = int(wallet)

# Create an empty basket
basket = []

# Loop through the dictionary
for item, price in items_purchase.items():

    # Clean the price string
    clean_price = price.replace("$", "").replace(",", "")

    # Convert price to integer
    item_price = int(clean_price)

    # Check if the item can be afforded
    if item_price <= wallet_amount:

        # Add item to basket
        basket.append(item)

        # Update wallet amount
        wallet_amount -= item_price

# Check if basket is empty
if len(basket) == 0:
    print("Nothing")

else:
    # Sort basket alphabetically
    basket.sort()

    # Display basket
    print(basket)