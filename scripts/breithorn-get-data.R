# This script prepares data for Breithorngletscher near Zermatt, Switzerland

## Setup project folder
data_path <- "../../data/"
results_path <- "../../results/"

## Get necessary functions 
source("../src/utils.R")

## Download data
# weather
download_file("https://raw.githubusercontent.com/mauro3/CORDS/master/data/workshop-reproducible-research/own/weather.dat",
              paste0(data_path,"weather.dat"))
download_file("https://raw.githubusercontent.com/mauro3/CORDS/master/data/workshop-reproducible-research/own/weather.info",
              paste0(data_path,"weather.info"))

# glacier mask
download_file("https://github.com/mauro3/CORDS/raw/master/data/workshop-reproducible-research/own/mask_breithorngletscher.zip",
              paste0(data_path,"mask_breithorngletscher.zip"))
unzip_one_file(paste0(data_path,"mask_breithorngletscher.zip"),
               NULL,
               data_path)

# digital elevation model (DEM)
download_file("https://github.com/mauro3/CORDS/raw/master/data/workshop-reproducible-research/foreign/swisstopo_dhm200_cropped.zip",
              paste0(data_path,"swisstopo_dhm200_cropped.zip"))
unzip_one_file(paste0(data_path,"swisstopo_dhm200_cropped.zip"),
               NULL,
               data_path)

## Some extra data, manually entered
z_weather_station = 2650 # elevation of weather station [m]
Ps0 = 0.005 # mean (and constant) precipitation rate [m/d]