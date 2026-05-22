# Create the Farm class
class Farm:

    # Constructor
    def __init__(self, farm_name):

        # Store farm name
        self.name = farm_name

        # Dictionary to store animals
        self.animals = {}

    # Add animals to the farm
    def add_animal(self, **kwargs):

        # Loop through keyword arguments
        for animal_type, count in kwargs.items():

            # Check if animal already exists
            if animal_type in self.animals:

                # Increase quantity
                self.animals[animal_type] += count

            else:
                # Add new animal
                self.animals[animal_type] = count

    # Display farm information
    def get_info(self):

        # Create result string
        info = self.name + "'s farm\n\n"

        # Add animals and counts
        for animal, count in self.animals.items():

            info += animal + " : " + str(count) + "\n"

        # Add final sentence
        info += "\n    E-I-E-I-0!"

        return info

    # Return sorted animal types
    def get_animal_types(self):

        return sorted(self.animals.keys())

    # Return short description
    def get_short_info(self):

        # Get sorted animal list
        animal_list = self.get_animal_types()

        # Create plural animal names
        plural_animals = []

        for animal in animal_list:

            # Add "s" if quantity is greater than 1
            if self.animals[animal] > 1:
                plural_animals.append(animal + "s")

            else:
                plural_animals.append(animal)

        # Create sentence
        if len(plural_animals) > 1:

            animals_text = ", ".join(plural_animals[:-1])
            animals_text += " and " + plural_animals[-1]

        else:
            animals_text = plural_animals[0]

        return self.name + "'s farm has " + animals_text + "."


# Test the class

# Create Farm object
macdonald = Farm("McDonald")

# Add animals
macdonald.add_animal(cow=5, sheep=2, goat=12)

# Display farm information
print(macdonald.get_info())

# Display sorted animal types
print(macdonald.get_animal_types())

# Display short description
print(macdonald.get_short_info())