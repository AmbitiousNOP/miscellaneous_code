#!/usr/bin/env Python
class Something(object):
    '''to be finished later '''   


class SomethingElse:
    pass


class YetAnotherType:
    pass



# Creaet a list of various instances of the above classes.
list_of_objects = [Something(), SomethingElse(), Something(), YetAnotherType(),
                   SomethingElse()]

fmt = "{:15}{}"
for obj in list_of_objects:
    print(fmt.format(type(obj).__name__, id(obj)))
