# -*- coding: utf-8 -*-
"""This script show a basic use of logging.

Created on: 03/03/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""

import logging

logging.basicConfig(
    filename='./log/results.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')

def sum_vals(a: int, b:int) -> int:
    """ Sums Two values
    Args:
        a: (int)
        b: (int)
    Return:
        a + b (int)
    """
    if not isinstance(a, int) or not isinstance(b, int):
        logging.error(msg="ERROR: a and b must have to be integers.")
        return 0

    try:
        logging.info("SUCCESS: Able to add a and b.")
        return a + b
    except TypeError:
        logging.error(msg="ERROR: a and b must have to be integers.")
        return 0


if __name__ == "__main__":
    sum_vals('no', 'way')
    sum_vals(4, 5)
