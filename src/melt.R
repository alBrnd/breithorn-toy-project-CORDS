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

## Net balance function at point location
net_balance_fn <- function(dt, Ts, Ps, melt_factor, T_threshold){
  
  # not working! stopifnot("Length of Ts and Ps is not the same",length(Ts) == length(Ps))
  
  total <- 0
  for(i in 1:length(Ts)){
    balance_rate = -melt(Ts[i], melt_factor) + accumulate(Ts[i], Ps[i], T_threshold)
    total = total + balance_rate * dt
  }
  return(total)
  
}

## Net balance over whole glacier 
glacier_net_balance_fn <- function(zs, dt, Ts, Ps, melt_factor, T_threshold, lapse_rate){
  
  glacier_net_balance  <- 0
  net_balance <- rep(0,length(zs))
  
  for(i in 1:length(zs)){
    for( j in 1:length(Ts)){
      TT <- lapse(Ts[j], zs[i], lapse_rate )
    }
    net_balance[i] <- net_balance_fn(dt, TT, Ps, melt_factor, T_threshold)
    glacier_net_balance <- glacier_net_balance + net_balance[i]
  }
  
  res <- data.frame(
    glacierBalance = glacier_net_balance/ length(zs),
    pointLocationBalance = net_balance
    
  )
  return(res)
}


