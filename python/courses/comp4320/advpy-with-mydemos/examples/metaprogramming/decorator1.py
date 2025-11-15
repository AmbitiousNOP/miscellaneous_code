# decorator1.py

# closure function
# nested function where inner 
# maintains state on return from outer
def print_msg(msg):
    some_string = "hello"
    
    def print_me(sep):
        print(some_string , msg, sep=sep)  # inner has access to outter data
    
    return print_me   # state of funtion is maintained on exit

func = print_msg("jenny")
func('##')

