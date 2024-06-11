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

# Function to unzip file
unzip_one_file <- function(zipfile,filename, destination_file){
  # make sure the directory exists
  if(!file.exists(zipfile)){
    print("File to unzip doesn't exist!")
  } else {
    unzip(zipfile= zipfile, files=filename, exdir = destination_file)
  }
}

# Usage:
# unzip_one_file("../../data/swissBOUNDARIES3D.zip", NULL, "../../data/swissBOUNDARIES3D/")
# unzip_one_file("../../data/swissBOUNDARIES3D.zip", "swissBOUNDARIES3D_1_5_TLM_BEZIRKSGEBIET.cpg", "../../data/swissBOUNDARIES3D2/")

# Function to read in Campbell data
read_campbell <- function(filename){

  dat <- read.table(filename, sep=",")
  y <- dat[,2]
  d <- dat[,3]
  hm <- dat[,4]
  t <- parse_campbell_date_time(y,d,hm)
  # go from 30min dt to 60 min
  t <- t[seq(1,length(t),by=2)]
  temp <- dat[seq(1,length(t),by=2),6]
  res <- data.frame(
    t = t,
    temp = temp
  )
  return(res)
}


parse_campbell_date_time <- function(year, day, HHMM){
  hour <- floor(HHMM/100)
  min <- HHMM - 100*hour
  return(day-1 + hour/24 + min/24/60)
}


