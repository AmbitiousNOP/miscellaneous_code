#!/usr/bin/env python
import sys
import getpass

name = getpass.getuser()

if name == 'root':
    print('do not run this utility as root')
elif name == 'guest':
    print('sorry - guests are not allowed to run this utility')
else:
    print('starting processing')
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    print(limit)
