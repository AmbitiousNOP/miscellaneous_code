#!/usr/bin/env python
import random
from multiprocessing import Pool


def main():
    POOL_SIZE = 30  # Number of processes

    # Read a line at a time from file into a list (removing new lines)
    with open('../data/words.txt') as words_in:
        word_list = [w.strip() for w in words_in]

    random.shuffle(word_list)  # Randomize word list

    pool = Pool(POOL_SIZE)  # Create pool with POOL_SIZE processes

    # Pass word_list to pool and get results
    # imap_unordered assigns values from list to process as needed
    upper_words = pool.imap_unordered(the_task, word_list)

    for word, _ in zip(upper_words, range(20)):  # Print just 20 the words
        print(word)


def the_task(word):  # Actual task to be completed
    return word.upper()


if __name__ == '__main__':
    main()
