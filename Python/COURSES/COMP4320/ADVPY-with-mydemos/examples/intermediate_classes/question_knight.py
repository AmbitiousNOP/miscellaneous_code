#!/usr/bin/env python
from knight import Knight


def main():
    k = Knight("Lancelot", "Sir", 'blue')

    # Bridgekeeper's question
    print(f'Sir {k.name}, what is your...favorite color?')  # property getter

    # Knight's answer
    print(f'red, no -- {k.color}!')  # property getter

    k.color = 'red'  # property setter

    print(f'color is now:{k.color}')  # property getter


if __name__ == '__main__':
    main()
