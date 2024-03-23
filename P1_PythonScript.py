# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:18:10 2024

@author: DNLROB007
"""

#%% Set paths

path_in = "C:/Users/DNLROB007/Documents/P1_Codes/P1_20240323_CTD20082911Depth_Temp_Sal_V1.dat"

#%% Import modules

import pandas as pd

#%% Read in data

ds = pd.read_csv(path_in, delimiter = "\t")
ds
