#!/usr/bin/env python
import tarfile
import os

# iterate over sample files
for tar_file in ('pres.tar', 'not_a.tar', 'textfiles.tar.gz'):
    filename = os.path.join('../data', tar_file)
    is_valid = tarfile.is_tarfile(filename)  # check to see if file is  tarfile
    text = 'IS' if is_valid else 'IS NOT'
    print("{} {} a tarfile".format(filename, text))
print()

with tarfile.open('../data/pres.tar') as tarfile_in:  # open tar file
    for member in tarfile_in:                      # iterate over members
        print(member.name, member.size)    # access member data
        
    print()

with tarfile.open('../data/pres.tar') as tarfile_in:
    # extract member to local file
    tarfile_in.extract('presidents.txt', path='../temp')

with tarfile.open('../data/textfiles.tar.gz') as tarfile_in:
    # extract member to local file
    tarfile_in.extract('knights.txt', path='../temp')

# open new tar archive for writing
with tarfile.open('../temp/text_files.tar', 'w') as tarfile_out:
    tarfile_out.add('../data/parrot.txt')      # add member
    tarfile_out.add('../data/alice.txt')       # add member

# open new tar archive for writing; archive is compressed with gzip
with tarfile.open('../temp/more_text_files.tar.gz', 'w:gz') as TAR:
    TAR.add('../data/parrot.txt')              # add member
    TAR.add('../data/alice.txt')               # add member
