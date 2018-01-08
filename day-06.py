"""
Day 06
List comprehensions, Dictionaries, Classes and objects
"""

LIST_NUMBERS = [2, 3, 8, 1, 10, 20, 4]
LIST_NAMES = ["Michael", " jon", "JANE"]
LIST_ALL = LIST_NUMBERS + LIST_NAMES

# multiply each item in the list by two using comprehension
print([item * 2 for item in LIST_NUMBERS])

# format names in list using comprehension
print(["my name is {}".format(person) for person in LIST_NAMES])

# Include only strings in the list using comprehensions
print([item for item in LIST_ALL if isinstance(item, str)])

# Format people name using comprehensions
print([person.lower().strip().capitalize() for person in LIST_NAMES])

# Dictionaries
def find_duplicated(data):
    """
    Find first duplicated char in data
    the solution is using a dictionary
    """
    checked_items = {}

    for item in data:
        if item in checked_items:
            return item
        else:
            checked_items[item] = 1

print(find_duplicated("ABCDEEAFZ"))

# Classes and objects
class Student:
    def __init__(self, name, school, grades):
        self.name = name
        self.school = school
        self.grades = grades

    def get_grades_total(self):
        return sum(self.grades)

JON_DOE = Student("Jon Doe", "Engineering", (80, 90, 100, 80, 85))
print("my name is {} I am a {} student and my grades are {}".format(JON_DOE.name, JON_DOE.school, JON_DOE.get_grades_total()))

JANE_DOE = Student("Jane Doe", "Business", (100, 90, 100, 95, 98))
print("my name is {} I am a {} student and my grades are {}".format(JANE_DOE.name, JANE_DOE.school, JANE_DOE.get_grades_total()))
