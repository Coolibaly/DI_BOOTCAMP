
# Exercice 1 : Converting Lists into Dictionaries ---------------------------------------------

print("Exercise 1: Converting Lists into Dictionaries\n")

# Create the lists
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Convert lists into a dictionary
result = dict(zip(keys, values))

# Display the dictionary
print(result)




# Exercice 2 : Cinemax n°2 ---------------------------------------------

print("\nExercise 2: Cinemax n°2\n")

family = {
    "rick": 43,
    "beth": 13,
    "morty": 5,
    "summer": 8
}

total_cost = 0

# Loop through the dictionary
for name, age in family.items():

    # Determine ticket price
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    # Add to total cost
    total_cost += price

    # Display ticket price
    print(name, "must pay $", price)

# Display total cost
print("Total cost:", total_cost)


print("-----------------------------------------bonus-----------------------------------------\n")

# Create an empty dictionary
custom_family = {}

# Ask how many family members
count = int(input("How many family members? "))

# Add members to the dictionary
for i in range(count):
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    custom_family[name] = age

# Calculate total
total = 0

for name, age in custom_family.items():

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    total += price

    print(name, "must pay $", price)

print("Total ticket cost:", total)


# Exercice 3 : Zara ---------------------------------------------

print("\nExercise 3: Zara\n")

# Create the dictionary
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

# Change number of stores
brand["number_stores"] = 2

# Print sentence
print("Zara clients are:", ", ".join(brand["type_of_clothes"]))

# Add country creation
brand["country_creation"] = "Spain"

# Add competitor if key exists
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

# Remove creation date
brand.pop("creation_date")

# Print last competitor
print(brand["international_competitors"][-1])

# Print US colors
print(brand["major_color"]["US"])

# Print number of keys
print(len(brand))

# Print all keys
print(brand.keys())


print("-----------------------------------------bonus-----------------------------------------\n")



more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

# Merge dictionaries
brand.update(more_on_zara)

# Display updated dictionary
print(brand)


# Exercice 4 : Some Geography ---------------------------------------------

print("\nExercise 4: Some Geography\n")

# Create the function
def describe_city(city, country="Unknown"):

    print(city, "is in", country + ".")


# Call the function
describe_city("Reykjavik", "Iceland")
describe_city("Paris")



# Exercice 5 : Random ---------------------------------------------


print("\nExercise 5: Random\n")

import random

# Create the function
def compare_numbers(user_number):

    # Generate random number
    random_number = random.randint(1, 100)

    # Compare numbers
    if user_number == random_number:
        print("Success!")
    else:
        print("Fail! Your number:", user_number,
              ", Random number:", random_number)


# Call the function
compare_numbers(50)



# Exercice 6 : Let’s create some personalized shirts ! ---------------------------------------------

print("\nExercise 6: Let’s create some personalized shirts !\n")

# Create the function
def make_shirt(size="large", text="I love Python"):

    print("The size of the shirt is", size,
          "and the text is", text + ".")


# Call the function
make_shirt()
make_shirt(size="medium")
make_shirt(size="small", text="Custom message")
make_shirt(text="Hello!", size="small")



# Exercice 7 : Temperature Advice ---------------------------------------------

print("\nExercise 7: Temperature Advice\n")

import random

# Create the function
def get_random_temp():

    return random.uniform(-10, 40)


# Create main function
def main():

    # Get random temperature
    temperature = get_random_temp()

    # Display temperature
    print("The temperature right now is",
          round(temperature, 1),
          "degrees Celsius.")

    # Give advice
    if temperature < 0:
        print("Brrr, that's freezing! Wear extra layers today.")
    elif temperature <= 16:
        print("Quite cold! Don't forget your coat.")
    elif temperature <= 23:
        print("Nice weather.")
    elif temperature <= 32:
        print("It's a bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")


# Call main function
main()


# Exercice 8 : Pizza Toppings ---------------------------------------------

print("\nExercise 8: Pizza Toppings\n")

# Create empty list
toppings = []

# Base price
price = 10

while True:

    # Ask user for topping
    topping = input("Enter a pizza topping (or type 'quit'): ")

    # Stop loop
    if topping.lower() == "quit":
        break

    # Add topping
    toppings.append(topping)

    # Increase price
    price += 2.5

    # Display message
    print("Adding", topping, "to your pizza.")

# Display final order
print("Pizza toppings:", toppings)
print("Total price: $", price)