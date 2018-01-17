"""
Day 15
Yet another algorithm: Binary Search
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int(low + high / 2)
        guess = arr[mid]

        if guess == target:
            return guess

        if guess < target:
            low = mid + 1

        if guess > target:
            high = mid - 1

print(binary_search([1, 2, 4, 7, 8, 9, 10, 20, 23, 55], 2))
