#!/usr/bin/env python
"""Sort titles, ignoring leading articles"""
import re

books = [
    "A Study in Scarlet", "The Sign of the Four", "The Valley of Fear",
    "The Hound of the Baskervilles", "The Adventures of Sherlock Holmes",
    "The Memoirs of Sherlock Holmes", "The Return of Sherlock Holmes",
    "His Last Bow", "The Case-Book of Sherlock Holmes"]

# compile regex to match leading articles
rx_article = re.compile(r'^(the|a|an)\s+', re.IGNORECASE)


# create function which takes element to compare and returns comparison key
def strip_articles(title):
    # strip off article and convert title to lower case
    return rx_article.sub('', title.lower())


for book in sorted(books, key=strip_articles):  # sort using custom function
    print(book)

print()