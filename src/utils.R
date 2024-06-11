# Function to get the git hash
gitHash <- function(basename, ext){
  fullHash <- system("git rev-parse HEAD", intern=TRUE)
  paste0(basename,'-',substring(fullHash,1, 10), '.',ext)
}

# Function to downlaod a file
download_file <- function(url, destination_file){
  if(file.exists(destination_file)){
    print(paste0("Already downloaded ", destination_file))
  } else {
    print(paste0("Downloading ", destination_file, " ..."))
    download.file(url=url, destfile = destination_file)
    print("Done!")
  }
}

# Usage :
# download_file("https://data.geo.admin.ch/ch.swisstopo.swissboundaries3d/swissboundaries3d_2024-01/swissboundaries3d_2024-01_2056_5728.shp.zip",
#              "../../data/swissBOUNDARIES3D.zip")