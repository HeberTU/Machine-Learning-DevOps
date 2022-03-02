# -*- coding: utf-8 -*-
"""
In this exercise we'll test different approaches to speed-up the way we find
common elements in two files: books_published_last_two_years.txt and
all_coding_books.txt.

Created on: 02/03/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""

import time
import numpy as np


def main():

    with open('./data/books_published_last_two_years.txt') as f:
        recent_books = f.read().split('\n')

    with open('./data/all_coding_books.txt') as f:
        coding_books = f.read().split('\n')

    # Approach 1: Loop Not recommended.
    start_time = time.time()

    recent_coding_books = []

    for book in recent_books:
        if book in coding_books:
            recent_coding_books.append(book)

    print(len(recent_coding_books))

    print(f'Approach 1 - Loop took: {time.time() - start_time}')

    # Approach 2: Vector operations with Numpy.
    start_time = time.time()

    recent_coding_books = np.intersect1d(
        ar1=recent_books,
        ar2=coding_books
    )

    print(len(recent_coding_books))

    print(f'Approach 2 - Numpy took: {time.time() - start_time}')

    # Approach 3: Sets.
    start_time = time.time()
    recent_coding_books = set(recent_books). \
        intersection(
        set(coding_books)
    )

    print(len(recent_coding_books))

    print(f'Approach 3 - Sets took: {time.time() - start_time}')


if __name__ == '__main__':
    main()
