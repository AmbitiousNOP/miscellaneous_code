#!/usr/bin/env python
from zipfile import ZipFile, ZIP_DEFLATED
import os
import os.path


# creating a zip file using context manager (with ... as)
with ZipFile("example.zip", mode="w", compression=ZIP_DEFLATED) as zip_file:
    for base in "parrot tyger knights alice breakfast mary".split():
        filename = f'{base}.txt'
        entry = os.path.join("../../data", filename)
        print(f"adding {entry} as {filename}")
        zip_file.write(entry, filename)  # Add member to zip file


# reading & extracting
destination = "extracted_files"
os.makedirs(destination, exist_ok=True)
with ZipFile("example.zip") as zip_file:  # Open zip file for reading
    print(zip_file.namelist())   # Print list of members in zip file
    print()

    # Read (raw binary) data from member and convert from bytes to string
    tyger = zip_file.read('tyger.txt').decode()
    print(tyger[:50])
    zip_file.extract('parrot.txt', path=destination)   # Extract member
