# -*- coding: utf-8 -*-
"""
Say your online gift store has one million users that each listed a gift on a
wish list. You have the prices for each of these gifts stored in gift_costs.txt.
For the holidays, you're going to give each customer their wish list gift for
free if it is under 25 dollars. Now, you want to calculate the total cost of
all gifts under 25 dollars to see how much you'd spend on free gifts.

Created on: 02/03/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""

import time
import numpy as np


def main():
    """Main function"""

    with open(
            file='./data/gift_costs.txt',
            encoding='UTF-8'
    ) as file:
        gift_costs = file.read().split('\n')

    gift_costs = np.array(
        object=gift_costs,
        dtype=int
    )

    # Approach 1: Loop Not recommended.
    start_time = time.time()

    total_price = 0

    for cost in gift_costs:
        if cost < 25:
            total_price += cost * 1.08

    print(total_price)

    print(f'Approach 1 - Loop took: {time.time() - start_time}')

    # Approach 2: Vector operations with Numpy.
    start_time = time.time()

    total_price = gift_costs[gift_costs < 25].sum() * 1.08

    print(total_price)

    print(f'Approach 2 - Numpy took: {time.time() - start_time}')


if __name__ == '__main__':
    main()
