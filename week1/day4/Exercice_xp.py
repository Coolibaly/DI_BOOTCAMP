# Exercice 1 : Animaux de compagnie

# Create the Pets class
class Pets:

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

# Create the Cat class
class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"

# Create Bengal class
class Bengal(Cat):

    def sing(self, sounds):
        return sounds

# Create Chartreux class
class Chartreux(Cat):

    def sing(self, sounds):
        return sounds

# Create Siamese class
class Siamese(Cat):

    def sing(self, sounds):
        return sounds

# Create cat objects
cat1 = Bengal("Leo", 2)
cat2 = Chartreux("Milo", 4)
cat3 = Siamese("Luna", 3)

# Create list of cats
all_cats = [cat1, cat2, cat3]

# Create Pets object
sara_pets = Pets(all_cats)

# Walk all cats
sara_pets.walk()











# Exercice 2 : Dogs

# Create Dog class
class Dog:

    def __init__(self, name, age, weight):

        self.name = name
        self.age = age
        self.weight = weight

    # Bark method
    def bark(self):

        return f"{self.name} is barking"

    # Run speed method
    def run_speed(self):

        return (self.weight / self.age) * 10

    # Fight method
    def fight(self, other_dog):

        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight"

        else:
            return f"{other_dog.name} won the fight"


# Create dog objects
dog1 = Dog("Rocky", 4, 20)
dog2 = Dog("Max", 5, 25)
dog3 = Dog("Buddy", 3, 18)

# Test methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))


# =========================================================
# Exercice 3 : Chiens domestiqués
# =========================================================

import random

# Create PetDog class
class PetDog(Dog):

    def __init__(self, name, age, weight):

        super().__init__(name, age, weight)

        self.trained = False

    # Train method
    def train(self):

        print(self.bark())

        self.trained = True

    # Play method
    def play(self, *args):

        dog_names = [self.name]

        for dog in args:
            dog_names.append(dog.name)

        print(", ".join(dog_names), "all play together")

    # Trick method
    def do_a_trick(self):

        if self.trained:

            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]

            print(f"{self.name} {random.choice(tricks)}")


# Create PetDog objects
pet1 = PetDog("Fido", 2, 10)
pet2 = PetDog("Charlie", 3, 15)
pet3 = PetDog("Oscar", 4, 12)

# Test methods
pet1.train()
pet1.play(pet2, pet3)
pet1.do_a_trick()


# =========================================================
# Exercice 4 : Cours en famille et par personne
# =========================================================

# Create Person class
class Person:

    def __init__(self, first_name, age):

        self.first_name = first_name
        self.age = age
        self.last_name = ""

    # Check if person is 18 or older
    def is_18(self):

        return self.age >= 18


# Create Family class
class Family:

    def __init__(self, last_name):

        self.last_name = last_name
        self.members = []

    # Add a new family member
    def born(self, first_name, age):

        person = Person(first_name, age)

        person.last_name = self.last_name

        self.members.append(person)

    # Check majority
    def check_majority(self, first_name):

        for person in self.members:

            if person.first_name == first_name:

                if person.is_18():

                    print(
                        "You are over 18, your parents Jane and John accept that you will go out with your friends"
                    )

                else:

                    print(
                        "Sorry, you are not allowed to go out with your friends."
                    )

    # Display family information
    def family_presentation(self):

        print("Family name:", self.last_name)

        for person in self.members:

            print(person.first_name, "-", person.age, "years old")


# Create Family object
family = Family("Smith")

# Add members
family.born("John", 45)
family.born("Jane", 42)
family.born("Emma", 17)
family.born("Lucas", 20)

# Test methods
family.check_majority("Emma")
family.check_majority("Lucas")

family.family_presentation()