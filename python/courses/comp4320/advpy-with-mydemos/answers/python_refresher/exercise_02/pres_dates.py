#!/usr/bin/env python

pres_lname = input("Enter president's last name: ")

with open("../../data/presidents.txt") as pres_in:
    for rec in pres_in:
        flds = rec.split(":")
        if flds[1] == pres_lname:
            death_date = flds[4]
            if death_date == "NONE":
                death_date == "***"

            print("NAME: {} {}".format(flds[2], flds[1]))
            print("BIRTH:", flds[3])
            print("DEATH:", death_date)
            print()
