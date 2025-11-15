#!/usr/bin/env python


def main():
    fruits = ["pomegranate", "cherry", "apricot", "date", "apple", "lemon",
              "kiwi", "orange", "lime", "watermelon", "guava", "papaya", "fig",
              "pear", "banana", "tamarind", "persimmon", "elderberry", "peach"]
    double = "\n" * 2

    # Pass str.upper as the callback
    print(process_list(fruits, str.upper), end=double)

    # Pass a lambda function as the callback
    print(process_list(fruits, lambda s: s[0].upper()), end=double)

    # Pass builtin function len() as the callback
    print(process_list(fruits, len), end=double)

    # Pass the result of process_list() to sum() to sum all the values

    print(sum(process_list(fruits, len)))


def process_list(alist, func):  # Accepts list and a  callback function
    # Call the callback function on each item as part of list comprehension
    return [func(item) for item in alist]


if __name__ == '__main__':
    main()
