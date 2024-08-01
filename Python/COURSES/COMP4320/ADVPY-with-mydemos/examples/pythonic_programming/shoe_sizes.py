#!/usr/bin/env python
BARLEYCORN = 1 / 3.0
CM_TO_INCH = 2.54
MENS_START_SIZE = 12
WOMENS_START_SIZE = 10.5

FMT = '{:6.1f} {:8.2f} {:8.2f}'
HEADFMT = '{:>6s} {:>8s} {:>8s}'
HEADINGS = ['Size', 'Inches', 'CM']

SIZE_RANGE = []
for i in range(6, 14):
    SIZE_RANGE.extend([i, i + .5])


def main():
    for heading, flag in [("MEN'S", True), ("WOMEN'S", False)]:
        print(heading)

        # format() expects individual arguments for each placeholder;
        # the asterisk unpacks HEADINGS into individual string arguments
        print((HEADFMT.format(*HEADINGS)))

        for size in SIZE_RANGE:
            inches, cm = get_length(size, flag)
            print(FMT.format(size, inches, cm))
            # The above print could have been written as:
            # print(FMT.format(size, *get_length(size, flag)))
            # by unpacking teh return value of get_length()
            # but tends to make it too busy and ahrd to read.
        print()


def get_length(size, mens=True):
    start_size = MENS_START_SIZE
    if not mens:
        start_size = WOMENS_START_SIZE

    inches = start_size - ((start_size - size) * BARLEYCORN)
    cm = inches * CM_TO_INCH
    return inches, cm


if __name__ == '__main__':
    main()
