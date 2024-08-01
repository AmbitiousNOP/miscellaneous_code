from typing import List, Tuple, NamedTuple, Dict, Union, Optional


class Animal:
    pass
class Dog(Animal):
    pass


my_nums: List[int]
my_nums = [1,2,3]

my_animals : List[Animal]
my_dogs  : List[Dog]

a1 = Animal()
d1 = Dog()
d2 = Dog()
d3 = Dog()

my_animals = [a1]
my_animals.append(d1)
dogs = [d1, d2]
my_animals.extend(dogs)
my_dogs = [d1]
my_dogs.extend(dogs)

my_dogs.append(a1)                  #mypy error

my_dogs.extend(my_animals)          #mypy error

class Person(NamedTuple):
    fn: str
    ln: str
    age: int

Person("Bob","Smith", 23)
Person("Sam","Smith", 23.5)          #mypy error


emps_dict : Dict[int, str] = {1: 'bob', 2: 'sue'}

emps_dict[3] = 23.5                  #mypy error
emps_dict[1] = Dog()                 #mypy error

width1 : Union[int, float] = 12
width2 : Union[int, float] = 5.7
width3 : Union[int, float] = '23'     #mypy error

width1 = 'six'                        #mypy error

class Animal2:
    def eat(self): pass

class Dog2(Animal2): pass
class Cat2(Animal2): pass
class Lizard(Animal2): pass

#only cats and dogs allowed to eat
def restricted_eat(animal: Union[Dog2, Cat2]) -> None:
    animal.eat()

a_dog: Dog2
restricted_eat(a_dog)

a_cat: Cat2
restricted_eat(a_cat)

a_lizard: Lizard
restricted_eat(a_lizard)             #mypy error


def get_user_id() -> Union[int, None]:
    return 1

def get_user_id2() -> Union[int, None]:
    return None

def get_user_id3() -> Union[int, None]:
    return 'done'                             #mypy error
    #print()                                  #mypy error  missing a return statement
    
def get_user_id4() -> Optional[int]:
    return 1

def get_user_id5() -> Optional[int]:     #expands to  Union[int, None]
    return 1

def get_user_id6() -> Optional[int]:
    return None

def get_user_id7() -> Optional[int]:
    return 'done'                            #mypy error
    #print()                                #mypy error  missing a return statement

