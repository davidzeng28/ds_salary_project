# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:43:28 2023

@author: David Zengs
"""

import glassdoor_scrapter as gs
import pandas as pd



df = gs.get_jobs('data scientist',1000, False, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
