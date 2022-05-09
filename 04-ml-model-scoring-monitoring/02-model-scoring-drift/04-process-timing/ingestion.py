# -*- coding: utf-8 -*-
"""Dummy ingestion file.

Created on: 9/5/22
@author: Heber Trujillo <heber.trj.urt@gmail.com>
Licence,
"""

import pandas as pd

ingested = pd.read_csv('samplefile.csv')

ingested.to_csv('samplefileingested.csv')
