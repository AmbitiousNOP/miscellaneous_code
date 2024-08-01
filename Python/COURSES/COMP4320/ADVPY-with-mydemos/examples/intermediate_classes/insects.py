#!/usr/bin/env python

from insect import Insect


if __name__ == '__main__':
    monarch = Insect('monarch butterfly', 'Mary', None)
    scarab = Insect('scarab beetle', 'Rupert', 'Bzzz', False)

    for insect in monarch, scarab:
        # can_fly is inhertited from Insect
        flying_status = "can" if insect.can_fly else "can't"

        fmt = "Hi! I am {} the {} and I {} fly!  {}"
        # name, species, and make_sound are all inherited from Animal
        print(fmt.format(insect.name, insect.species, flying_status,
                         insect.make_sound()))
