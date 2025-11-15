#!/usr/bin/env python


def all_primes(limit):
    flags = set()  # initialize empty set (to be used for "is-prime" flags

    for i in range(2, limit):
        if i in flags:
            continue
        for j in range(2 * i, limit + 1, i):
            flags.add(j)  # add non-prime elements to set
        yield i  # execution stops here until next value is requested


np = all_primes(50)  # next_prime() returns a generator object
for prime in np:      # iterate over *yielded* primes
    if prime == 37: break
    print(prime, end=' ')
print()
