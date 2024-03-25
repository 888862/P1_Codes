# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:18:10 2024

@author: DNLROB007
"""

#%% Set paths

path_in = "C:/Users/DNLROB007/Documents/P1_Codes/P1_20240323_CTD20082911Depth_Temp_Sal_V1.dat"

#%% Import modules

import pandas as pd
import matplotlib.pyplot as plt

#%% Read in data

ds = pd.read_csv(path_in, delimiter = "\t")
ds

#%% Plot temperature and salinity on two different panels

fig, ax = plt.subplots(1, 2)

# Addressing the top left Axes as index 0
ax[0].plot(ds["Temp(C)"], ds["Depth(m)"], color = 'b')
ax[0].set_xlabel("Temperature (Degrees celsius)")
ax[0].set_ylabel("Depth (m)")

#Plot Salinity vs depth, index 1
ax[1].plot(ds["Salinity(psu)"], ds["Depth(m)"], color = 'r')
ax[1].set_xlabel("Salinity (psu)")

plt.show

#%%
