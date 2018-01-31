"""
Day 09
Decorators
"""

import functools

def do_something(method):
    @functools.wraps(method)
    def my_decorator():
        print("at decorator")
        method()
        print("after")
    
    return my_decorator

@do_something
def my_function():
    print("my function")

my_function()

def decorator_with_args(n):
    def my_decorator(method):
        @functools.wraps(method)
        def run_method():
            print("inside decorator #2")
            if n == 27:
                print("number is {}".format(n))
                method()
            else:
                print("number isn't 27")

        return run_method
    return my_decorator

@decorator_with_args(27)
def say_something():
    print("hello")

say_something()