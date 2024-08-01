#!/usr/bin/env python
from unicode_blocks import UnicodeBlock

def create__menu():
    menu = {}
    for ascii_value, unicode_block in enumerate(UnicodeBlock, start=65):
        ascii_char = chr(ascii_value)
        menu[ascii_char] = unicode_block
    return menu

def print_menu(menu):
    for char, unicode_block in menu.items():
        print(f'{char} -- {unicode_block.name}')
    print()

def prompt_user():
    prompt = "Enter a letter from the menu for\nthe desired Unicode block > "
    return input(prompt).upper()

def main():
    # print MiscellaneousSymbols
    menu = create__menu()
    print_menu(menu)
    user_choice = prompt_user()

    if user_choice not in menu:
        print(user_choice, " is not one of the menu options")
        return

    for char in menu[user_choice].characters():
        print(char, end="  ")
    print()

if __name__ == "__main__":
    main()
