#!/usr/bin/env Python
from access import Access


a = Access()
# accessing both the 'public_method' attribute
# and the instance data attribute 'a'
a.public_method()
print(a.a)
print()

# accessing both the '_private_method' attribute
# and the instance data '_b' attribute
a._private_method()     # legal, but is intended to be private
print(a._b)             # legal, but is also intended to be private
print()

# attempt to access the '__mangled_method' attribute
try:
    a.__mangled_method()    # does not exist under this name
except AttributeError as ae:
    print(ae)
print()

# knowing how it is mangled though still provides access
a._Access__mangled_method()
print(a._Access__c)
print()
