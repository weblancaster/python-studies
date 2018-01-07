"""
Day 05
Some built-in functions, keyword arguments, infinite args
"""

INT_TO_STR = isinstance(str(5), str)
print("integer to string: {}".format(INT_TO_STR))

FLOAT_TO_STR = isinstance(str(5.5), str)
print("float to string: {}".format(FLOAT_TO_STR))

BOOLEAN_TO_STR = isinstance(str(True), str)
print("boolean to string: {}".format(BOOLEAN_TO_STR))

STR_TO_INT = isinstance(int("5"), int)
print("string to integer: {}".format(STR_TO_INT))

STR_TO_FLOAT = isinstance(float("5.5"), float)
print("string to float: {}".format(STR_TO_FLOAT))

STR_TO_BOOLEAN = isinstance(bool("True"), bool)
print("string to boolean: {}".format(STR_TO_BOOLEAN))

print("list not sorted {} and sorted {}".format([10, 30, 1, 0], sorted([10, 30, 1, 0])))

# Keyword arguments
def person_message(name="Jon Doe", age=25):
    """
    Return persons name and age
    """
    return "My name is {} and I am {} years old.".format(name, age)

print(person_message("Michael"))
print(person_message(age=27, name="michael")) # no need to send args in order as long you add keyword arguments

# Infinite arguments
def get_fruits(*fruits):
    """
    Return fruits name
    """
    for fruit in fruits:
        print("{} is delicious".format(fruit.capitalize()))

get_fruits("orange", "banana", "berries", "apple") # for the sake of trying out infinite args this is not send as a list but individual args
