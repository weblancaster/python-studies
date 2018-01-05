"""
Day 03
I woke in the middle of the last night with my first earthquake experience
that kept me awake for an 1h or so. That being sad, tonight I go to bed "early"
so I decided to write some simple algorithms
"""

# List comprehensions
print([x * 2 for x in range(5)])
print([x * 2 for x in range(5) if x == 2])
# I will come back to list comprehensions later

MULTI_LIST = [1, 2, "michael", ["another", "list", [10, 20]]]

def flatten_list(my_list):
    """
    Wrapper used to flat the list
    """
    flat_list = []

    def flat(my_list):
        """
        Recursively flat list
        """
        for item in my_list:
            if isinstance(item, list):
                return flat(item)
            else:
                flat_list.append(item)

    flat(my_list)
    return flat_list

print(flatten_list(MULTI_LIST))