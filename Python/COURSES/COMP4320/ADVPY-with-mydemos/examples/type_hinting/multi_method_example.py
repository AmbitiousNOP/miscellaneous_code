from multimethod import multimethod, DispatchError
from some_dataclasses import Location, Music, Fish


@multimethod
def drop_bass(loc: Location, m: Music):
    print('WUBWUBWUBWUBWUBWUB DRRRRRR')


@multimethod                    #type: ignore
def drop_bass(loc: Location, f: Fish):  
    print('Sploosh')


drop_bass(Location("Band Practice"), Music("Classic Rock"))
drop_bass(Location("State Park"), Fish("Trout"))

try:
    drop_bass("This should", "Not be allowed")
except DispatchError as de:
    print("Dispatch Error:", de)
