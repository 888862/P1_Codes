# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:18:10 2024

@author: DNLROB007
"""

#%% Set paths

path_in = "C:/Users/DNLROB007/Documents/P1_Codes/CTDdata_20082911_Depth_Temp_Sal.dat"

#%% Import modules

import pandas as pd

#%% Read in data

ds = pd.read_csv(path_in, delimiter = "\t")
ds
