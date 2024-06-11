# Import melt.R functions
source("../src/melt.R")
source("../src/utils.R")

# Define the synthetic weather and glacier
synthetic_T <- function(t){
  T <- -10 * cos(2 * pi / 365 * t) - 8 * cos(2 * pi * t) + 5
  return(T)
}

synthetic_P <- function(t){
  return(rep(0.008, length(t)))
}

synthetic_glacier <- function(){
  x <- seq(from=0, to=10, length.out=100)  # x coordinates
  elevation <- seq(from=1000, to=2000, length.out=100)
  res <- data.frame(
    x = x,
    elevation = elevation
  )
  return(res)
}

# Define constants
lapse_rate <- -0.6 / 100
melt_factor <- 0.005
T_threshold <- 4
dt <- 1 / 24
t <- seq(from=0, to=365 + dt, by=dt) 

# Plot the synthetic weather
Ts <- synthetic_T(t)
png(filename=gitHash(paste0('../../results/',Sys.Date(),'SyntheticTemperature'),'png')) # To export the file
plot(t,Ts, main="Synthetic Temperature", xlab='Time (days)', ylab='Temperature (°C)', type = 'l')
dev.off()

# Run the model for one year at a point
ele <- 1500
Ts_ele <- lapse(Ts, dt, lapse_rate)  
Ps <- synthetic_P(t)

net_balance_fn(dt, Ts, Ps, melt_factor, T_threshold)

# # Run the model for one year for the whole glacier
# xs <- synthetic_glacier()[,1]
# zs <- synthetic_glacier()[,2]
# Ts <- synthetic_T(t)
# 
# total_massbalance <- glacier_net_balance_fn(zs, dt, Ts, Ps, melt_factor, T_threshold, lapse_rate)[,1]
# point_massbalance <- glacier_net_balance_fn(zs, dt, Ts, Ps, melt_factor, T_threshold, lapse_rate)[,2]
# plot(xs, point_massbalance, main='Glacier Mass Balance', ylab='Mass balance', xlab='Distance (km)')

## Generate output table
# make a table of mass-balance for different temperature offsets and store it
# # Loop over temperature offsets and store the results in a DataFrame
# total_MB
# point_MB
# Ts_ <- seq(-4,5,by=dT)
# for(dT in -4:5) {
#   total_MB <- c(total_MB, glacier_net_balance_fn(zs, dT, Ts_, Ps, melt_factor, T_threshold, lapse_rate)[,1])
#   point_MB <- c(point_MB, glacier_net_balance_fn(zs, dT, Ts_, Ps, melt_factor, T_threshold, lapse_rate)[,2])
# }
# 
# # Append the results to the list
# out <- data.frame(
#   dt = Ts_,
#   total_massbalance = total_MB,
#   point_massbalance =  point_MB
# )
# 
# # Convert the list of results to a DataFrame
# df = pd.DataFrame(out)
# 
# # Display the DataFrame
# print(df)

# Store the git hash in the results folder
gitHash(paste0(Sys.Date(),'GlacierMassBalance'),'txt')
gitLog <- system('git log', intern = TRUE)

write(gitLog, file = gitHash(paste0('../../results/',Sys.Date(),'GitLog'),'txt'), append = FALSE)
