#!/usr/bin/python
import datetime


def main():
    info = []
    with open('../../data/presidents.txt') as pres_in:
        for line in pres_in:
            (term, last_name, first_name, birth_date,
             death_date, birth_dateplace, birth_state,
             start_date, end_date, party) = line.rstrip().split(':')
               # ' '.join( (first_name, last_name) )
            
            info.append( ( f"{first_name} {last_name}", birth_date, party ) )

    by_birth_date = sorted(info, key=lambda x: x[1])
    fmt = "{:32} {:15}{}"
    print(fmt.format("Name", "Birth Date", "Affiliation(s)"))
    for pres in by_birth_date:
        print(fmt.format(*pres))


if __name__ == '__main__':
    main()
