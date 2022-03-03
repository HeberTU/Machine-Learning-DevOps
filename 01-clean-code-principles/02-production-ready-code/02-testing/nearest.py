# -*- coding: utf-8 -*-
"""Dummy function for testing.

Created on: 03/03/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""

def nearest_square(num: int)->int:
    """ Return the nearest perfect square
    that is less or equal to num."""
    root = 0
    while (root + 1) ** 2 <= num:
        root += 1
    return root ** 2