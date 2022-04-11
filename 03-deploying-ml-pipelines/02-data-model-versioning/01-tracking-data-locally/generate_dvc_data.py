# -*- coding: utf-8 -*-
"""Tracking Data Locally with DVC.

Created on: 4/11/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
import logging
import argparse
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)-15s %(message)s"
)
logger = logging.getLogger()


def main(factor: float) -> None:
    """This function generate and write a pandas DataFrame."""

    logger.info("Generating data")

    numbers = [x * factor for x in range(0, 11)]

    data = pd.DataFrame(
        data={
            'numbers': numbers
        }
    )

    logger.info("Writing data")
    data.to_csv("./dvc-data.csv")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="This is a dvd demo script."
    )

    parser.add_argument(
        "--factor",
        type=float,
        help="rescale factor",
        required=False,
        default=1
    )

    args = parser.parse_args()

    main(factor=args.factor)
