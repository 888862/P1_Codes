# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:25:25 2024

@author: DNLROB007
"""

#%% Set paths

path_in = "C:/Users/DNLROB007/Documents/P1_Codes/SAA2_WC_2017_metocean_10min_avg.csv"
path_out = "C:/Users/DNLROB007/Documents/P1_Codes"

#%% Import modules

import pandas as pd
import matplotlib.pyplot as plt

#%% Read in data

ds = pd.read_csv(path_in, delimiter = ",", #parse_dates = ["TIME_SERVER"], index_col = "TIME_SERVER", 
                 na_values=['', '-', 'NA', 'nan'])
ds

#%% Clean data by removing NAN values
#ds = ds.dropna()

#%% Slice data until 4th July
#sliced_data = ds["2017-06-28 17:10:00" : "2017-07-04 23:50:00"]
sliced_data = ds.iloc[0:905]

#dr = pd.date_range("2017-06-28 17:10:00" , "2017-07-04 23:50:00", freq = "1440T")
#%% Plot timeseries of Temperature

xticks = sliced_data["TIME_SERVER"]

plt.style.use("grayscale")
fig, ax = plt.subplots()
ax.plot(xticks, sliced_data["TSG_TEMP"])
ax.set_xticks(xticks[::100])
ax.set_xticklabels(xticks[::100], rotation=90)
ax.set_xlabel("Time")
ax.set_ylabel("Sea surface temperature (degrees celsius)")
plt.show()
fig.savefig("SST_timeseries.png")

#%%Plotting a histogram

plt.style.use("default")
fig, ax =plt.subplots()
ax.hist(sliced_data["TSG_SALINITY"], label="Salinity (psu)",bins=[30, 30.5, 31, 31.5, 32, 32.5, 33, 33.5, 34, 34.5, 35])
ax.set_xlabel("Salinity (psu)")
ax.set_ylabel("# of observations")
#ax.legend()
plt.show()

#%%Scatterplot

plt.style.use("default")
fig, ax = plt.subplots()
ax.scatter(sliced_data["WIND_SPEED_TRUE"], sliced_data["AIR_TEMPERATURE"],           
           c=sliced_data["LATITUDE"])
ax.set_xlabel("Wind speed (m/s)")
ax.set_ylabel("Air Temperature (degrees Celsius)")
plt.colorbar(ax.scatter(sliced_data["WIND_SPEED_TRUE"], sliced_data["AIR_TEMPERATURE"],           
           c=sliced_data["LATITUDE"]),label = "Latitude (ddmm)")
plt.show()

fig.savefig("SST_timeseries.png", dpi = 200)

#%%





































