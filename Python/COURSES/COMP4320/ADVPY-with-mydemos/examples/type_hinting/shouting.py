#!/usr/bin/env python
"""Function type hinting example"""


def shout(times: int = 1, *args: str, **kwargs: int) -> str:
    for word in args:
        print(word.upper() * times)
    print("-" * 30)
    for word, times in kwargs.items():
        print(word.upper() * times)
    #return ''

def main() -> None:
    shout(2,  "Hello", "Goodbye")
    print()
    print("#" * 30)
    shout(3, "Something", "Something Else", alpha=3, beta=5, gamma=4)


if __name__ == '__main__':
    main()
