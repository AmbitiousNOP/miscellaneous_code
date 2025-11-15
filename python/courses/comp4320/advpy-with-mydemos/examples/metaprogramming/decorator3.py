# decorator3.py

# Decorator pattern
# decorator is a function that takes another function as param and returns it
# allows adding functionality to existing function
# without modifying existing function
# wrapper
# more elegant way to accomplish this than  closure pattern
import sys
def display_data(func):
    def inner():
        print("Running", func.__name__, "function",'from', sys._getframe(  ).f_code.co_name)
        func()
        print("Finished inner func")
    
    return inner

@display_data
def print_data():
    print("Hello World")


print_data()
print("All done")
