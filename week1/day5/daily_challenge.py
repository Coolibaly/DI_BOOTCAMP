# Circle Class (OOP + Dunder Methods)

import math


class Circle:

    # Constructor
    def __init__(self, radius):

        self.radius = radius

    # Alternative constructor (from diameter)
    @classmethod
    def from_diameter(cls, diameter):

        radius = diameter / 2
        return cls(radius)

    # Property: diameter
    @property
    def diameter(self):

        return self.radius * 2

    # Area of circle
    def area(self):

        return math.pi * (self.radius ** 2)

    # String representation
    def __str__(self):

        return f"Circle(radius={self.radius})"

    def __repr__(self):

        return self.__str__()

    # Add two circles
    def __add__(self, other):

        if not isinstance(other, Circle):
            return NotImplemented

        return Circle(self.radius + other.radius)

    # Greater than comparison
    def __gt__(self, other):

        return self.radius > other.radius

    # Equality comparison
    def __eq__(self, other):

        return self.radius == other.radius

    # Less than (for sorting)
    def __lt__(self, other):

        return self.radius < other.radius


# TESTING

# Create circles
c1 = Circle(3)
c2 = Circle.from_diameter(10)
c3 = Circle(5)

# Print circles
print(c1)
print(c2)

# Area
print("Area c1:", c1.area())

# Addition
c4 = c1 + c3
print("c1 + c3 =", c4)

# Comparisons
print("c1 > c3:", c1 > c3)
print("c1 == c3:", c1 == c3)

# Sorting circles
circles = [c1, c2, c3, c4]
circles_sorted = sorted(circles)

print("Sorted circles:", circles_sorted)