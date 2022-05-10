# -*- coding: utf-8 -*-
"""Dummy ingestion file.

Created on: 9/5/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""
from pathlib import Path
import pandas as pd

ROOT_PATH = Path(__file__).resolve().parents[0]

ingested = pd.read_csv(ROOT_PATH / 'samplefile.csv')

ingested.to_csv(ROOT_PATH / 'samplefileingested.csv', index=False)
