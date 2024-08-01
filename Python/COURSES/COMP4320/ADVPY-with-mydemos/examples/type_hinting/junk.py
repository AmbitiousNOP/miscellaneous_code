#!/usr/bin/env python
from typing import Union, List


class Engine:
    def drain_oil(self):
        print("Draining Oil")


class Refrigerator:
    def remove_door(self):
        print("Removing door for safety reasons")


class ACUnit:
    def recycle_freon(self):
        print("Recycling freon")


def destroy(junk: Union[Refrigerator, ACUnit, Engine]) -> None:
    if isinstance(junk, Refrigerator):
        junk.remove_door()
    elif isinstance(junk, Engine):
        junk.drain_oil()
    else:
        #junk.drain_oil()
        junk.recycle_freon()
        
'''
items: List = [ACUnit(), Refrigerator(), Engine()]
for item in items:
    destroy(item)
print()
'''