# -*- coding: utf-8 -*-
"""Timing demo script.

Created on: 9/5/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
import os
import sys
import glob
import timeit
from typing import List, Dict
from pathlib import Path
import numpy as np


def get_file_name(script_path: Path) -> str:
    """Get script name from script's fully qualified path.

    Args:
        script_path: script's fully qualified path

    Returns:
        script_name.
    """

    return str(script_path).split("/")[-1]


def get_python_files(path: Path) -> List[Path]:
    """Read all csv file within path directory tree.

    Args:
        path: path from which the recursive reading will start.

    Returns:
        file_paths: List of absolute file paths.

    """
    file_paths = []
    for root, dirs, files in os.walk(path):
        files = glob.glob(os.path.join(root, '*.py'))
        for f in files:
            print(__file__)
            if get_file_name(f) != get_file_name(__file__):

                file_paths.append(os.path.abspath(f))

    return file_paths


def process_timing(script_path: Path) -> float:
    """Measure time to execute a process.

    Args:
        script_path: script's fully qualified path

    Returns:
        process_time: time in sec. requires to run the process

    """
    starttime = timeit.default_timer()

    os.system(f'python {script_path}')

    return timeit.default_timer() - starttime


def benchmark_process(script_path: Path, n: int = 20) -> Dict[str, float]:
    """Run python process n times to calculate timing statistics.

    Args:
        script_path: script's fully qualified path.
        n: times to repeat the process.

    Returns:
        statistics: run time statistics.

    """
    measures = []

    for i in range(n):
        process_time = process_timing(script_path)
        measures.append(process_time)

    measures = np.array(measures)

    return {
        'mean': measures.mean(),
        'std': measures.std(),
        'min': measures.min(),
        'max': measures.max(),
    }


if __name__ == '__main__':

    ROOT_PATH = Path(__file__).resolve().parents[0]

    script_urls = get_python_files(path=ROOT_PATH)

    print(benchmark_process(script_path=script_urls[0]))