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


def net_balance_fn(dt, Ts, Ps, melt_factor, T_threshold):
    """
    Integrate the balance rate (this is at a point) over time for given temperature and precipitation arrays to get the "net balance".

    Args:
        dt: The time step.
        Ts: Array of temperatures.
        Ps: Array of precipitations.
        melt_factor: The factor to compute melt amount.
        T_threshold: The temperature threshold for accumulation.

    Returns:
        net balance (this is at a point)
    """
    assert len(Ts) == len(Ps)
    total = 0.0
    for T, P in zip(Ts, Ps):
        balance_rate = -melt(T, melt_factor) + accumulate(T, P, T_threshold)
        total += balance_rate * dt
    return total


def glacier_net_balance_fn(zs, dt, Ts, Ps, melt_factor, T_threshold, lapse_rate):
    """
    Calculate:
    - the glacier net balance (integration of balance rate over time and space)
    - the net balance at each point (integration of balance rate over time)

    Args:
        zs: Array of elevations (with the weather station as datum)
        dt: The time step.
        Ts: Array of temperatures.
        Ps: Array of precipitations.
        melt_factor: The factor to compute melt amount.
        T_threshold: The temperature threshold for accumulation.
        lapse_rate: The lapse rate (temperature change per unit elevation change).

    Returns:
        the glacier net balance [m]
        net balance at all points [m]
    """
    glacier_net_balance = 0.0
    net_balance = np.zeros(len(zs))
    for i, z in enumerate(zs):
        TT = [lapse(T, z, lapse_rate) for T in Ts]
        net_balance[i] = net_balance_fn(dt, TT, Ps, melt_factor, T_threshold)
        glacier_net_balance += net_balance[i]
    return glacier_net_balance / len(zs), net_balance



# if __name__ == '__main__':
#     assert melt(-5, melt_factor=2) == 0, "Test failed: Melt rate should be 0 for T < 0"
#     assert accumulate(5, 10, 0) == 0, "Test failed: Accumulation should be 0 for T > T_threshold"
#     assert accumulate(-5, 10, 0) == 10, "Test failed: Accumulation should be equal to precipitation for T <= T_threshold"

    


