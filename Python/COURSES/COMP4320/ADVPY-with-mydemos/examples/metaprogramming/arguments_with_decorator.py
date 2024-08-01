#!/usr/bin/env python
from spam_decorator_with_args import spam


def main():
    print(ham())


@spam(2, 3)
def ham():
    return "Ham"


if __name__ == '__main__':
    main()
