#!/usr/bin/env python

def sibling_rivalry(siblings, friends):
    return (sib for sib in siblings if sib not in friends)


myfriends = 'alan bob jane sue'.split()
mysibs = 'alan mark sue alice'.split()
sibriv = sibling_rivalry(mysibs, myfriends)
print(sibriv)
for s in sibriv:
    print(s)