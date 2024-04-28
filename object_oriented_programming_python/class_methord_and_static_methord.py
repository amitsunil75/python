# Class methods and static methods are two types of methods in Python that are defined within a class. 
# They serve different purposes and are invoked differently.

# **Class Methods**:
# - Class methods are bound to the class itself rather than an instance of the class.
# - They are defined using the `@classmethod` decorator.
# - They receive the class itself (`cls`) as the first parameter, allowing them to access and modify class-level variables.
# - They can be used as alternative constructors or to modify class-level attributes.


class MyClass:
    class_variable = 10

    @classmethod
    def modify_class_variable(cls, value):
        cls.class_variable = value

# Accessing class method
MyClass.modify_class_variable(20)

# Accessing modified class variable
print(MyClass.class_variable)  # Output: 20

# **Static Methods**:
# - Static methods are not bound to either the class or instances of the class.
# - They are defined using the `@staticmethod` decorator.
# - They do not receive the class or instance as parameters.
# - They are primarily used for utility functions that are related to the class but do not require access to instance or class variables.


class MyClass:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

# Accessing static method
print(MyClass.is_even(4))  # Output: True


# **Key Differences**:
# - Class methods are bound to the class and receive the class itself (`cls`) as the first parameter, while static methods are
#  not bound to the class or instances and do not receive any special parameters.
# - Class methods are commonly used for operations involving class-level variables or alternative constructors, while
#  static methods are used for utility functions that are related to the class but do not require access to instance or class variables.

# Understanding the distinction between class methods and static methods helps in writing cleaner 
# and more maintainable code in Python's object-oriented paradigm.