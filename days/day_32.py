"""
Day 32
Stacks
"""

class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        self.list.pop(self.size() - 1)
    
    def peek(self):
        if self.size() > 0:
            return self.list[self.size() - 1]
        
        return None
    
    def clear(self):
        self.list = []
    
    def size(self):
        return len(self.list)

books = Stack()
print(books.push("jon doe"))
print(books.push("jane doe"))
print(books.push("jose doe"))
print(books.size())
print(books.peek())
print(books.pop())
print(books.peek())