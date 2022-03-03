# -*- coding: utf-8 -*-
"""This script show how to handle error.

Created on: 02/03/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from typing import Optional


def divide_vals(numerator: float, denominator: float) -> Optional[float]:
    """Divides two numbers.

    Args:
        numerator: (float) numerator of fraction
        denominator: (float) denominator of fraction

    Returns:
        fraction_val: (float) numerator/denominator
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Denominator cannot be zero")


def num_words(text: str) -> Optional[int]:
    """Count the number of words.

    Args:
        text: (string) string of words

    Returns:
        num_words: (int) number of words in the string
    """
    try:
        num_words = len(text.split())

        return num_words

    except AttributeError:

        print("Text argument must be a string")


if __name__ == "__main__":

    divide_vals(numerator=1, denominator=0)
    num_words(text=0)
