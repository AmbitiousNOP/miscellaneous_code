# decorator2.py

# Before decorator pattern

def print_data():
    print("Hello World")
    
def display_data(func):
    def inner():
        print("Running", func.__name__, "function")
        func()
        print("Finished inner func")
    
    return inner

decor_func = display_data(print_data)
decor_func()

print("All done")
