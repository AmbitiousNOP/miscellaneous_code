from abc import ABCMeta, abstractmethod


# metaclasses control how classes are created;
# metaclass=ABCMeta adds restrictions to classes that inherit from Animal
class Animal(metaclass=ABCMeta):
    @abstractmethod               # decorates speak as an abstract method
    def speak(self):
        pass

    def fn(self):
        print('fn...')
        
# Often easier to write using the ABC helper class as shown below:

# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
