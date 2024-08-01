#!/usr/bin/env python
from president import President


def main():
    for term in 1, 26, 39, 45:
        p = President(term)
        print(p)
        print()


if __name__ == "__main__":
    main()
