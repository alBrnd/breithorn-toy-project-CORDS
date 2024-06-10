## GLACIER MASS BALANCE - Functions

## Melt rate function
melt <- function(T, melt_factor){
  if(T>=0){
    meltrate <- melt_factor*T
  } else {
    meltrate <- 0
  }
  return(meltrate)
}

## Accumulation rate function
accumulate <- function(T, P, T_threshold){
  if(T<=T_threshold){
    accumulation <- P
  } else {
    accumulation <- 0
  }
  return(accumulation)
}

## Lapsed-temperature function
lapse <- function(T, dz, lapse_rate){
  lapsed_T <- lapse_rate*dz + T
  return(lapsed_T)
}

## Synthetic temperature function
temp <- function(t){
  synth_T <- -10*cos(2*pi/364 * t) - 8*cos(2*pi*t) + 5
  return(synth_T)
}

## Synthetic precipitation function
precip <- function(t){
  return(8e-3)
}



