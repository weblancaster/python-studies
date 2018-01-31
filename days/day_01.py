"""
Day 01
Getting acclimated with the sintax and some API quirks
"""

GRADES = [77, 80, 90]
TUPLE_GRADES = (77, 80, 90) # immutable
SET_GRADES = {77, 80, 90} # Unique & unordered

# List
print("<< List >>")
GRADES.append(100)
print(GRADES)

GRADES.insert(1, "intruder")
print(GRADES)

# Tuple
print("<< Tuple >>")
TUPLE_GRADES = TUPLE_GRADES + (100, "another one") # needs comma otherwise it's just a number and not a tuple
print(TUPLE_GRADES)

# Set
print("<< SET >>")
SET_GRADES.add(100)
SET_ANOTHER_ONE = {77, 80, 90}
print(SET_GRADES.difference(SET_ANOTHER_ONE))
print(SET_GRADES.union(SET_ANOTHER_ONE))
print(SET_GRADES.intersection(SET_ANOTHER_ONE))