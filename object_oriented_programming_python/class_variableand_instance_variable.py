# Class variables and instance variables are two types of variables in Python's object-oriented programming paradigm.
#  They serve different purposes and have distinct scopes and lifetimes.

# **Class Variables**:
# - Class variables are shared among all instances of a class.
# - They are defined within the class but outside of any methods.
# - They are accessed using the class name, not instance names.
# - They are useful for storing data that is common to all instances of the class.


class MyClass:
    class_variable = 10

# Accessing class variable
print(MyClass.class_variable)  # Output: 10

# Modifying class variable
MyClass.class_variable = 20
print(MyClass.class_variable)  # Output: 20


# **Instance Variables**:
# - Instance variables are unique to each instance of a class.
# - They are defined within methods using `self`.
# - They are accessed using instance names.
# - They are useful for storing data specific to each instance of the class.

class MyClass:
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

# Creating instances
obj1 = MyClass(100)
obj2 = MyClass(200)

# Accessing instance variables
print(obj1.instance_variable)  # Output: 100
print(obj2.instance_variable)  # Output: 200

# Modifying instance variables
obj1.instance_variable = 150
print(obj1.instance_variable)  # Output: 150


# **Key Differences**:
# - Class variables are shared among all instances, while instance variables are unique to each instance.
# - Class variables are defined outside of methods, while instance variables are defined within methods using `self`.
# - Class variables are accessed using the class name, while instance variables are accessed using instance names.

# Understanding the distinction between class variables and instance variables is crucial for effective object-oriented
#  programming in Python.