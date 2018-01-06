"""
Day 04
I'm taking my time in looking more into list comprehensions so here is a bubble sort
just so I don't miss a day writting python
"""

def bubble_sort(arr):
    """
    Sort list: lowest to highest
    """
    swapped = True

    while swapped:
        swapped = False
        i = 0

        while i < len(arr) - 1:
            current = arr[i]
            right = arr[i + 1]

            if current > right:
                swapped = True
                arr[i + 1] = current
                arr[i] = right

            if current == right:
                pass

            i += 1

    return arr


print(bubble_sort([2, 3, 8, 1, 10, 20, 4]))