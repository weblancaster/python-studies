"""
Day 02
More playing around but now with loops and condition flows
"""

STR = "name"
PEOPLE = ["jon", "jane", "bruce", "leonard", "sheldon"]
TUPLE_PEOPLE = ("jon", "jane", "bruce", "leonard", "sheldon") # immutable
SET_PEOPLE = {"jon", "jane", "bruce", "leonard", "sheldon"}

def spacer():
    """
    Print a space
    """
    print(" ")

def str_loop():
    """
    Iterate over a string
    """
    spacer()
    for char in STR:
        print("string (for in) is {}".format(char))

def list_loop():
    """
    Iterate over a list
    """

    counter = 0
    spacer()

    for number in PEOPLE:
        print("list (for in) is {}".format(number))

    while counter < len(PEOPLE):
        print("list (while) is {}".format(PEOPLE[counter]))
        counter = counter + 1
    
    if "jon" in PEOPLE:
        print("there is a jon in the PEOPLE")

    if "michael" not in PEOPLE:
        print("no michael in the PEOPLE")

def tuple_loop():
    """
    Iterate over a tuple
    """
    counter = 0
    spacer()

    for person in TUPLE_PEOPLE:
        print("tuple (for in) is {}".format(person))

    while counter < len(TUPLE_PEOPLE):
        print("tuple (while) is {}".format(PEOPLE[counter]))
        counter = counter + 1
    
    if "jon" in TUPLE_PEOPLE:
        print("there is a jon in the TUPLE_PEOPLE")

    if "michael" not in TUPLE_PEOPLE:
        print("no michael in the TUPLE_PEOPLE")

def set_loop():
    """
    Iterate over a Set
    """
    spacer()
    counter = 0

    for person in SET_PEOPLE:
        print("set (for in) is {}".format(person))
    
    while counter < len(SET_PEOPLE):
        print("set (while) is {}".format(PEOPLE[counter]))
        counter = counter + 1
    
    if "jon" in SET_PEOPLE:
        print("there is a jon in the SET_PEOPLE")

    if "michael" not in SET_PEOPLE:
        print("no michael in the SET_PEOPLE")

def str_play(str):
    """
    Basic string to list and some cleanup/formatting
    """
    spacer()
    names = str.split(",")
    formatted_names = []

    for name in names:
        formatted_names.append(name.strip())

    print(formatted_names)


str_loop()
list_loop()
tuple_loop()
set_loop()
str_play("jon , jane, bruce , leonard , sheldon ")
