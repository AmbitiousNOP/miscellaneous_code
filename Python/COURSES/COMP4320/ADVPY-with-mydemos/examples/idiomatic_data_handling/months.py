#!/usr/bin/env python
from month_enum import Month

feb =  Month.February

print(feb.name, "can be shortened to", feb.short_name,
      f"and has {feb.value[1]} days in it")

for month in Month:
    print(f'{month:^20}', end="")
    if month.value[0] % 4 == 0:
        print()
