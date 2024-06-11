## Setup project folder
data_path <- "../../data/"
results_path <- "../../results/"

## Get necessary functions 
source("../src/utils.R")
source("breithorn-model-paras.R")

## Get necessary libraries
library(raster)

## Read data
weather <- read_campbell(paste0(data_path,"weather.dat"))
t <- weather$t
Ts <- weather$temp
dem <- raster(paste0(data_path,"swisstopo_dhm200_cropped/dhm200_cropped.asc"))
mask <- raster(paste0(data_path,"mask_breithorngletscher/mask_breithorngletscher.asc"))
Ps <- rep(Ps0,length(Ts)) 

## Visualize input data
png(filename=gitHash(paste0(results_path,Sys.Date(),'SyntheticTemperature'),'png')) # To export the file
plot(t,Ts, type="l", main="Recorded Temperatures", xlab="time", ylab="Temperature (°C)")
dev.off()

png(filename=gitHash(paste0(results_path,Sys.Date(),'dem'),'png')) # To export the file
plot(dem, main="Digital Elevation Model")
dev.off()

png(filename=gitHash(paste0(results_path,Sys.Date(),'mask'),'png')) # To export the file
plot(mask, main="Glacier Mask")
dev.off()


