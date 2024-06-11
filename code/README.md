## toy research project
---

## Glacier Mass Balance Model

This project is a simple glacier mass balance model implemented in Python. The model calculates glacier melt rates, accumulation rates, and integrates these over time and space to determine the net glacier mass balance. It also generates synthetic weather data for temperature and precipitation.

### Folder Structure

```
.
├── src
│   ├── melt.py
│   └── utils.py
├── scripts
│   └── simple.py
├── tests
│   └── test-melt.py
├── README.md
```

### Files

- **src/melt.py**: Contains core functions for calculating melt rates, accumulation rates, and net balance.
- **src/utils.py**: Contains utility functions, including a function to generate versioned filenames using the current git hash.
- **scripts/simple.py**: A script that imports functions from `melt.py` and `utils.py` to run the glacier mass balance model and generate plots.
- **tests/test-melt.py**: Contains unit tests for the `melt.py` functions using the `pytest` framework.

### Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install dependencies**:
    ```bash
    pip install numpy pandas matplotlib gitpython pytest
    ```

### Usage

#### 1. Running the Model

To run the glacier mass balance model, execute the `simple.py` script:

```bash
python scripts/simple.py
```

#### 2. Generating Versioned Filenames

The `generate_versioned_filename` function in `utils.py` generates filenames that include the current git commit hash and an optional `-dirty` suffix if there are uncommitted changes. This is useful for keeping track of model runs.

#### 3. Plotting Results

The `simple.py` script generates plots of synthetic temperature data and glacier mass balance, saving the plots with versioned filenames.

### Running Tests

To run the tests, use `pytest`:

```bash
pytest tests/test-melt.py
```

#### `tests/test-melt.py`

This file contains unit tests for the functions in `melt.py`.



### Functions

#### `melt.py`

- **melt(T, melt_factor)**
  - Calculates the glacier melt rate based on temperature and melt factor.
  - **Parameters**:
    - `T` (float): Temperature at a given altitude and time.
    - `melt_factor` (float): Melt factor to scale the melt rate.
  - **Returns**: float - Melt rate.

- **accumulate(T, P, T_threshold)**
  - Calculates the accumulation on the glacier based on temperature, precipitation, and a temperature threshold.
  - **Parameters**:
    - `T` (float): Temperature at a given altitude and time.
    - `P` (float): Precipitation on the glacier.
    - `T_threshold` (float): Temperature threshold below which snow starts accumulating.
  - **Returns**: float - Accumulation.

- **lapse(T, dz, lapse_rate)**
  - Calculates the temperature lapse rate.
  - **Parameters**:
    - `T` (float): Temperature at a given altitude and time.
    - `dz` (float): Change in elevation.
    - `lapse_rate` (float): Lapse rate (temperature change per unit elevation change).
  - **Returns**: float - Lapsed temperature.

- **net_balance_fn(dt, Ts, Ps, melt_factor, T_threshold)**
  - Integrates the balance rate over time for given temperature and precipitation arrays to get the net balance.
  - **Parameters**:
    - `dt` (float): Time step.
    - `Ts` (array): Array of temperatures.
    - `Ps` (array): Array of precipitations.
    - `melt_factor` (float): Melt factor.
    - `T_threshold` (float): Temperature threshold for accumulation.
  - **Returns**: float - Net balance.

- **glacier_net_balance_fn(zs, dt, Ts, Ps, melt_factor, T_threshold, lapse_rate)**
  - Calculates the glacier net balance over time and space.
  - **Parameters**:
    - `zs` (array): Array of elevations.
    - `dt` (float): Time step.
    - `Ts` (array): Array of temperatures.
    - `Ps` (array): Array of precipitations.
    - `melt_factor` (float): Melt factor.
    - `T_threshold` (float): Temperature threshold for accumulation.
    - `lapse_rate` (float): Lapse rate.
  - **Returns**: tuple - (glacier net balance, net balance at each point).

#### `utils.py`

- **generate_versioned_filename(basename, ext)**
  - Generates a filename with the current git hash and optionally appends `-dirty` if there are uncommitted changes.
  - **Parameters**:
    - `basename` (str): Base name of the file.
    - `ext` (str): File extension.
  - **Returns**: str - Generated filename.

#### `simple.py`

- **synthetic_T(t)**
  - Generates synthetic temperature data.
  - **Parameters**:
    - `t` (array): Array of time steps.
  - **Returns**: array - Synthetic temperature data.

- **synthetic_P(t)**
  - Generates synthetic precipitation data.
  - **Parameters**:
    - `t` (array): Array of time steps.
  - **Returns**: array - Synthetic precipitation data.

- **synthetic_glacier()**
  - Generates synthetic glacier data.
  - **Returns**: tuple - (x coordinates, elevation values).

### Example

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import melt
import utils

# Define constants
lapse_rate = -0.6 / 100
melt_factor = 0.005
T_threshold = 4
dt = 1 / 24
t = np.arange(0, 365 + dt, dt)

# Generate synthetic data
Ts = synthetic_T(t)
Ps = synthetic_P(t)

# Run the model
xs, zs = synthetic_glacier()
total_massbalance, point_massbalance = melt.glacier_net_balance_fn(zs, dt, Ts, Ps, melt_factor, T_threshold, lapse_rate)

# Plot results
plt.figure()
plt.plot(xs, point_massbalance)
plt.xlabel('Distance (km)')
plt.ylabel('Point Mass Balance')
plt.title('Glacier Mass Balance')
versioned_filename = utils.generate_versioned_filename('glacier_mass_balance', 'png')
plt.savefig(versioned_filename)
plt.show()
```

### License

This project is licensed under the MIT License. See the LICENSE file for details.

---

This README provides an overview of the glacier mass balance model, instructions for running the model and tests, descriptions of the key functions, and example usage. Adjust the example and function details to fit the specifics of your implementation if necessary.
