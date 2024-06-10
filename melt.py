# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 08:37:32 2024

@author: Bornand
"""

# toy research project: glacier mass balance

# melt rate

# signature: (T, melt_factor) -> meltrate (m/d)

def melt(T, melt_factor):
    """
    Calculate the glacier melt rate based on temperature and melt factor.

    Parameters:
    T (float): Temperature at a given altitude and time.
    melt_factor (float): Melt factor to scale the melt rate.

    Returns:
    float: Melt rate.
    """
    if T >= 0:
        return melt_factor * T
    else:
        return 0


## Accumulation rate function
def accumulate(T, P, T_threshold):
    """
    Calculate the accumulation on the glacier based on temperature, a temperature threshold and precipitation.

    Parameters:
    T (float): Temperature at a given altitude and time.
    P (float): Precipitation on the glacier.
    T_threshold (float): Temperature threshold below which the snow starts accumulating the precipitation
    Returns:
    float: accumulation.
    """
  if T <= T_threshold :
    return P
  else: 
    return 0



# # Example usage:
# temperature = 5  # Example temperature in degrees Celsius
# melt_factor = 0.1  # Example melt factor
# melt_rate = melt(temperature, melt_factor)
# print(f"Melt rate: {melt_rate}")



def lapse(T, dz, lapse_rate):
      """
    Calculate the glacier lapse rate based on temperature.

    Parameters:
    T (float): Temperature at a given altitude and time.
    lapse_rate: 

    Returns:
    float: lapsed temperature
    """  
    
    lapsed_T = lapse_rate*dz + T
    return lapsed_T

