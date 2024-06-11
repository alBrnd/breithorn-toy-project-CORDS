# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:00:14 2024

@author: Bornand
"""

import os
import sys
# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import utils

# This script prepares data for Breithorngletscher near Zermatt, Switzerland

## Setup project folder
main_path = "D:/CORDS/Breithorn-project"
os.makedirs(os.path.dirname(os.path.join(main_path, "/code")), exist_ok=True)
code_path = os.path.join(main_path, "code/")
data_path = os.makedirs(os.path.dirname(os.path.join(main_path, "/data")), exist_ok=True)
data_path = os.path.join(main_path, "data/")
results_path = os.makedirs(os.path.dirname(os.path.join(main_path, "/results")), exist_ok=True)
results_path = os.path.join(main_path, "results/")

## Download data
# weather
destination_file = os.path.join(data_path, "weather.dat")
utils.download_file("https://raw.githubusercontent.com/mauro3/CORDS/master/data/workshop-reproducible-research/own/weather.dat", destination_file)

# glacier mask
destination_file_glacier = os.path.join(data_path, "mask_breithorngletscher.zip")
utils.download_file("https://github.com/mauro3/CORDS/raw/master/data/workshop-reproducible-research/own/mask_breithorngletscher.zip", destination_file_glacier)

zipfile_path = destination_file_glacier
filename = 'mask_breithorngletscher/mask_breithorngletscher.asc'
destination_file = 'D:/CORDS/Breithorn-project/data/mask_breithorngletscher.asc'
utils.unzip_one_file(zipfile_path, filename, destination_file)

# digital elevation model (DEM)
destination_file_dem = os.path.join(data_path, "swisstopo_dhm200_cropped.zip")
utils.download_file("https://github.com/mauro3/CORDS/raw/master/data/workshop-reproducible-research/foreign/swisstopo_dhm200_cropped.zip", destination_file_dem)

zipfile_path = destination_file_dem
filename = 'swisstopo_dhm200_cropped/dhm200_cropped.asc'
destination_file = 'D:/CORDS/Breithorn-project/data/dhm200_cropped.asc'
utils.unzip_one_file(zipfile_path, filename, destination_file)


## Some extra data, manually entered
z_weather_station = 2650 # elevation of weather station [m]
Ps0 = 0.005 # mean (and constant) precipitation rate [m/d]