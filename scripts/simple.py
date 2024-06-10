# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:18:57 2024

@author: Bornand
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd

# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Now you can import functions from melt.py
import melt


# Define the synthetic weather and glacier
def synthetic_T(t):
    # Implement the function to generate synthetic temperature
    T = -10 * np.cos(2 * np.pi / 365 * t) - 8 * np.cos(2 * np.pi * t) + 5
    return(T)

def synthetic_P(t):
    # Implement the function to generate synthetic precipitation
    return([0.008]*len(t))


def synthetic_glacier():
    # Implement the function to generate synthetic glacier data
    # For example:
    x = np.linspace(0, 10, 100)  # x coordinates
    elevation = np.linspace(1000, 2000, 100)  # Elevation values
    return x, elevation

# Define constants
lapse_rate = -0.6 / 100
melt_factor = 0.005
T_threshold = 4
dt = 1 / 24
t = np.arange(0, 365 + dt, dt)

# Plot the synthetic weather
Ts = synthetic_T(t)
plt.figure()
plt.plot(t, Ts)
plt.xlabel('Time (days)')
plt.ylabel('Temperature (°C)')
plt.title('Synthetic Temperature')
plt.show()

# Run the model for one year at a point
ele = 1500
Ts_ele = melt.lapse(Ts, dt, lapse_rate)  
Ps = synthetic_P(t)


melt.net_balance_fn(dt, Ts, Ps, melt_factor, T_threshold)

# Run the model for one year for the whole glacier
xs, zs = synthetic_glacier()
Ts = synthetic_T(t)

total_massbalance, point_massbalance = melt.glacier_net_balance_fn(zs, dt, Ts, Ps, melt_factor, T_threshold, lapse_rate)
plt.figure()
plt.plot(xs, point_massbalance)
plt.xlabel('Distance (km)')
plt.ylabel('Total Mass Balance')
plt.title('Glacier Mass Balance')
plt.show()

## Generate output table
# make a table of mass-balance for different temperature offsets and store it
# out = []
# for dT in range(-4, 5):
#     Ts_ = synthetic_T(t) + dT
#     # run model
#     total_massbalance, point_massbalance = melt.glacier_net_balance_fn(zs, dT, Ts_, Ps, melt_factor, T_threshold, lapse_rate)
#     out[]
#     # store in ou

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
