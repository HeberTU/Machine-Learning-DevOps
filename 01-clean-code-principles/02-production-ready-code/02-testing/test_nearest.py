# -*- coding: utf-8 -*-
"""Testing pytest suit for nearest function.

Created on: 03/03/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from nearest import nearest_square

def test_nearest_square_5():
    assert (nearest_square(5) == 4)

def test_nearest_square_n12():
    assert (nearest_square(-12) == 0)

def test_nearest_square_9():
    assert (nearest_square(9) == 9)

def test_nearest_square_23():
    assert (nearest_square(23) == 16)