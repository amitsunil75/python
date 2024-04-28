class MyColour:
    def myColour(self):
        print('blue')
class YourColour(MyColour):
    def myColour(self):
        print('Brown')


yourColor=YourColour()
print(yourColor.myColour())

# Create a class `Shape` with a method `area()` that calculates the area of the shape. Then, create subclasses `Rectangle` and `Circle` that inherit from `Shape` and override the `area()` method to calculate the area of a rectangle and a circle, respectively.


import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Example usage
rectangle = Rectangle(4, 5)
print("Area of Rectangle:", rectangle.area())  # Output: 20

circle = Circle(3)
print("Area of Circle:", circle.area())  # Output: ~28.27
# ```

# **Explanation**:

# - We first define a base class `Shape` with a method `area()` that returns `0`. This method will be overridden in the subclasses.
# - We then define a subclass `Rectangle` that inherits from `Shape`. It has an `__init__` method to initialize the length and width of the rectangle and overrides the `area()` method to calculate the area of the rectangle using the formula `length * width`.
# - Similarly, we define another subclass `Circle` that inherits from `Shape`. It has an `__init__` method to initialize the radius of the circle and overrides the `area()` method to calculate the area of the circle using the formula `π * radius^2`.
# - In the example usage, we create instances of `Rectangle` and `Circle` and call their `area()` methods to calculate their respective areas.

# This example demonstrates method overriding in Python, where subclasses provide a specific implementation of a method defined in their superclass. This allows objects of different classes to be treated uniformly, providing flexibility and code reuse.