# Getter and setter methods are special methods used to access and modify the values of private attributes within a class in Python. They provide controlled access to the attributes, allowing validation and encapsulation of the class's data.

# **Getter Method**:
# - A getter method, also known as an accessor method, is used to retrieve the value of a private attribute.
# - It typically has a name that starts with `get`, followed by the name of the attribute being accessed.
# - It does not directly modify the attribute's value but returns it for external use.

class MyClass:
    def __init__(self):
        self._value = 0  # Private attribute

    # Getter method for _value
    def get_value(self):
        return self._value

# Example usage
obj = MyClass()
print(obj.get_value())  # Output: 0

# **Setter Method**:
# - A setter method, also known as a mutator method, is used to modify the value of a private attribute.
# - It typically has a name that starts with `set`, followed by the name of the attribute being modified.
# - It receives the new value as a parameter and performs any necessary validation or processing before assigning it to the attribute.


class MyClass:
    def __init__(self):
        self._value = 0  # Private attribute

    # Setter method for _value
    def set_value(self, new_value):
        if new_value >= 0:
            self._value = new_value
        else:
            print("Invalid value. Value must be non-negative.")

# Example usage
obj = MyClass()
obj.set_value(10)
print(obj.get_value())  # Output: 10

obj.set_value(-5)  # Output: Invalid value. Value must be non-negative.
print(obj.get_value())  # Output: 10 (Value remains unchanged)


# **Key Points**:
# - Getter and setter methods provide controlled access to private attributes, allowing validation and encapsulation of data.
# - Getter methods retrieve the value of an attribute, while setter methods modify the value of an attribute after validation.
# - They help enforce data integrity and encapsulation within a class, making the class's interface more robust and predictable.