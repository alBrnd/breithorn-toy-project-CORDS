# Function to get the git hash
gitHash <- function(basename, ext){
  fullHash <- system("git rev-parse HEAD", intern=TRUE)
  paste0(basename,'-',substring(fullHash,1, 10), '.',ext)
}