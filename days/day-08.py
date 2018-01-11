"""
Day 08
More classes but now inheritance and some Lambda functions
"""

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


jon = Student("Jon Doe", "MIT")
jane = WorkingStudent("Jane Doe", "MIT", "25000")
friend = WorkingStudent.friend(jane, "Dave", 22000)

print("My name is {} and I go to school at {}".format(jon.name, jon.school))
print("{} is a student at {} and an employee with salary at {}".format(jane.name, jane.school, jane.salary))

# Lambda functions

def calc_n(method):
    return method()

LIST = [10, 29, 12]

print("# Lambda functions")
print(calc_n(lambda: 25 * 2))
print(list(filter(lambda x: x != 12, LIST)))
