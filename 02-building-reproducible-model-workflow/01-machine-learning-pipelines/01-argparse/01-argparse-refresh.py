# -*- coding: utf-8 -*-
"""A Brief Refresher on Python Scripting with Argparse

Created on: 3/14/2022
@author: Heber Trujillo <heber.trj.urt@gmail.com> 
Licence,
"""
import logging
import argparse

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def main(number: float, text: str) -> None:

    logger.debug("This is a debug message")

    logger.info("This is an info message")

    logger.warning("This is a warning")

    logger.error("This is an error")

    logger.info(f"Number argument {number}")

    logger.info(f"Text argument {text}")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="This is a brief description of this script")

    parser.add_argument(
        "--number", type=float, help="Number input", required=True
    )

    parser.add_argument(
        "--text", type=str, help="String input", required=False,
        default="Hello"
    )

    args = parser.parse_args()

    main(number=args.number, text=args.text)
