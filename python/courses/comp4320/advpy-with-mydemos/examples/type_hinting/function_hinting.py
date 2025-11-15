#!/usr/bin/env python
"""Function type hinting example"""


def repeat(word: str, times: int = 1) -> str:
    return word * times


def main() -> None:
    print(repeat("Absolutely", 4))
    
    # Python interpreter permits the following
    # But the mypy module will flag it as an issue
    print(repeat(5, 6))


if __name__ == '__main__':
    main()
   
