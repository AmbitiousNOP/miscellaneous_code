#!/usr/bin/env python
from spam_decorator import spam


def main():
    print(ham())


@spam  # The spam decorator automatically wraps ham()
def ham():
    return "Ham"


if __name__ == '__main__':
    main()
