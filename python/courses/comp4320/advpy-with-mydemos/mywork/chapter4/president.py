"""
Create a module that implements a President class.
● This class has a constructor that takes the index number of the president (1-45) and creates an object
containing the associated information from the presidents.txt file.
● Provide the following properties (types indicated after ->):

term_number -> int
first_name -> string
last_name -> string
birth_date -> date object
death_date -> date object (or None, if still alive)
birth_place -> string
birth_state -> string
term_start_date -> date object
term_end_date -> date object (or None, if still in office)
party -> string

"""


class President():
    with open("/home/cjpenn/miscellaneous_code/Python/COURSES/COMP4320/ADVPY-with-mydemos/data/presidents.txt") as f:
        list_of_presidents = [tuple(i.split(":"))
                              for i in (f.read().split("\n"))[:-1]]

    def __init__(self, president_number):
        self.president_number = president_number
        self.term_number = President.list_of_presidents[president_number-1][0]
        self.first_name = President.list_of_presidents[president_number-1][1]
        self.last_name = President.list_of_presidents[president_number-1][2]
        self.birth_date = President.list_of_presidents[president_number-1][3]
        self.death_date = President.list_of_presidents[president_number-1][4]
        self.birth_place = President.list_of_presidents[president_number-1][5]
        self.birth_state = President.list_of_presidents[president_number-1][6]
        self.term_start_date = President.list_of_presidents[president_number-1][7]
        self.term_end_date = President.list_of_presidents[president_number-1][8]
        self.part = President.list_of_presidents[president_number-1][9]
