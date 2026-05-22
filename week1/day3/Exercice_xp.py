# Exercise 1 : Cats

# Create the Cat class
class Cat:

    # Constructor
    def __init__(self, cat_name, cat_age):

        self.name = cat_name
        self.age = cat_age


# Create cat objects
cat1 = Cat("Milo", 2)
cat2 = Cat("Luna", 5)
cat3 = Cat("Simba", 3)


# Function to find the oldest cat
def find_oldest_cat(cat1, cat2, cat3):

    oldest = cat1

    if cat2.age > oldest.age:
        oldest = cat2

    if cat3.age > oldest.age:
        oldest = cat3

    return oldest


# Get the oldest cat
oldest_cat = find_oldest_cat(cat1, cat2, cat3)

# Print result
print("The oldest cat is", oldest_cat.name,
      "and is", oldest_cat.age, "years old.")


# Exercise 2 : Dogs

# Create the Dog class
class Dog:

    # Constructor
    def __init__(self, name, height):

        self.name = name
        self.height = height

    # Bark method
    def bark(self):

        print(self.name, "goes woof!")

    # Jump method
    def jump(self):

        print(self.name, "jumps", self.height * 2, "cm high!")


# Create dog objects
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Buddy", 35)

# Print dog details
print(davids_dog.name, "is", davids_dog.height, "cm tall.")
davids_dog.bark()
davids_dog.jump()

print(sarahs_dog.name, "is", sarahs_dog.height, "cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()

# Compare dog sizes
if davids_dog.height > sarahs_dog.height:
    print(davids_dog.name, "is bigger than", sarahs_dog.name)

else:
    print(sarahs_dog.name, "is bigger than", davids_dog.name)


# Exercise 3 : Who’s the song producer?

# Create the Song class
class Song:

    # Constructor
    def __init__(self, lyrics):

        self.lyrics = lyrics

    # Method to print lyrics
    def sing_me_a_song(self):

        for line in self.lyrics:
            print(line)


# Create a Song object
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Print lyrics
stairway.sing_me_a_song()


# Exercise 4 : Afternoon at the Zoo

# Create the Zoo class
class Zoo:

    # Constructor
    def __init__(self, zoo_name):

        self.zoo_name = zoo_name
        self.animals = []
        self.groups = {}

    # Add animals
    def add_animal(self, *new_animals):

        for animal in new_animals:

            if animal not in self.animals:
                self.animals.append(animal)

    # Display animals
    def get_animals(self):

        print("Animals in the zoo:")

        for animal in self.animals:
            print(animal)

    # Sell animal
    def sell_animal(self, animal_sold):

        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    # Sort and group animals
    def sort_animals(self):

        # Sort animals alphabetically
        sorted_animals = sorted(self.animals)

        # Create empty dictionary
        self.groups = {}

        # Group animals by first letter
        for animal in sorted_animals:

            first_letter = animal[0]

            if first_letter not in self.groups:
                self.groups[first_letter] = []

            self.groups[first_letter].append(animal)

    # Display groups
    def get_groups(self):

        for letter, animals in self.groups.items():
            print(letter + ":", animals)


# Create Zoo object
brooklyn_safari = Zoo("Brooklyn Safari")

# Add animals
brooklyn_safari.add_animal(
    "Giraffe",
    "Bear",
    "Baboon",
    "Lion",
    "Zebra",
    "Cat",
    "Cougar"
)

# Display animals
brooklyn_safari.get_animals()

# Sell an animal
brooklyn_safari.sell_animal("Bear")

# Display animals again
brooklyn_safari.get_animals()

# Sort and group animals
brooklyn_safari.sort_animals()

# Display groups
brooklyn_safari.get_groups()