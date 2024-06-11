# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:41:40 2024

@author: Bornand
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd
import rasterio
# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# import functions from melt.py and utils.py
import melt
import utils

main_path = "D:/CORDS/Breithorn-project"
os.chdir(main_path)
results_path = os.path.join(main_path, "results/")

## Read data
weather_fl = "./data/weather.dat"
t, Ts = utils.read_campbell(weather_fl)
dem_reader = rasterio.open('./data/dhm200_cropped.asc')
dem = dem_reader.read(1)
mask_reader = rasterio.open('./data/mask_breithorngletscher.asc')
mask = mask_reader.read(1)

## Set model parameters
lapse_rate = -0.6/100
melt_factor = 0.005
T_threshold = 4

Ps = Ps0 .+ Ts*0; # make precipitation a vector of same length as Ts

plt.plot(t, Ts)
plt.xlabel('Time (days)')
plt.ylabel('Temperature (°C)')
plt.title('Synthetic Temperature')
plt.show()

# Select glacier points and use elevation of weather station as datum
zs = dem[mask == 1] - z_weather_station

# Calculate the time step
dt = t[1] - t[0]

# Run the model for the whole glacier
total_massbalance, point_massbalance = melt.glacier_net_balance_fn(zs, dt, Ts, Ps, melt_factor, T_threshold, lapse_rate)

# Make a map of the point mass balance
point_massbalance_map = np.full_like(dem, np.nan)
point_massbalance_map[mask == 1] = point_massbalance

# Plot the mass balance map
plt.figure(figsize=(10, 8))
plt.imshow(point_massbalance_map, cmap='viridis', interpolation='none')
plt.colorbar(label='Point Mass Balance (mm w.e.)')
plt.title('Breithorn Glacier Mass Balance')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')

# Generate the versioned filename and save the plot
output_filename = utils.generate_versioned_filename(os.path.join(results_dir, "breithorn_massbalance_field"), ".png")
plt.savefig(output_filename)
plt.close()

# Initialize an empty list to store the results
out = []

# Loop over temperature offsets and store the results in a DataFrame
for dT in range(-4, 5):
    Ts_ = synthetic_T(t) + dT
    total_massbalance, point_massbalance = melt.glacier_net_balance_fn(zs, dT, Ts_, Ps, melt_factor, T_threshold, lapse_rate)
    # Append the results to the list
    out.append({
        'dT': dT,
        'total_massbalance': total_massbalance,
        'point_massbalance': point_massbalance
    })

# Convert the list of results to a DataFrame
df = pd.DataFrame(out)

# Display the DataFrame
print(df)

# Generate the versioned filename
basename = "glacier_mass_balance_overTemperature"
ext = "csv"
versioned_filename_df = utils.generate_versioned_filename(basename, ext)
df.to_csv(results_path+versioned_filename_df)
