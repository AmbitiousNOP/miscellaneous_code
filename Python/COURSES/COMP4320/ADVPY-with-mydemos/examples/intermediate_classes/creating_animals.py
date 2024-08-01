#!/usr/bin/env python
from animal import Animal


def main():
    animals = [Animal("African lion", "Leo", "Roarrrrrrr"),
               Animal("cat", "Garfield", "Meowwwww"),
               Animal("cat", "Felix", "Meowwwww")]

    for animal in animals:
        print(animal.name, "is a", animal.species, "--", animal.make_sound())


if __name__ == "__main__":
    main()
