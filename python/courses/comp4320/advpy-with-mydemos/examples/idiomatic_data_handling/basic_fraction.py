from dataclasses import dataclass


@dataclass (init=True, eq=True, order=True)
class Fraction:
    num: int  
    denom: int 
    extra: int = 1   # extra with defualrs
# ctor auto generated with params for each prop

def addme(x, y):
    pass

f1 = Fraction(1, 2)     # ctor auto generated
f2 = Fraction(3, 4)
f3 = Fraction(num=1,denom=2)

f4 = Fraction(3, 4, 99)

print(f1 == f2)
print(f1 == f3)

print(f1 < f2)
print(f3 < f1)
print(f2 >= f1)

f1.addme = addme

f1.addme(f1, f2)