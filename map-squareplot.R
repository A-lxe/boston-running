## Source: https://github.com/tejaykodali/Chicago-mvt-data/blob/master/chicagoMVT.r

library(ggplot2)
library(dplyr)
library(tidyr)
library(maps)
library(ggmap)

## Reading in the data
chicagoMVT <- read.csv('trees-frequencymap.csv', stringsAsFactors = FALSE)
chicagoMVT$frequency <- chicagoMVT$frequency
## Get Chicago map
chicago <- get_map(location = 'Boston', zoom=13)

## Get crime locations
locationCrimes <- as.data.frame(chicagoMVT)
names(locationCrimes) <- c('long', 'lat', 'frequency')
locationCrimes$long <- as.numeric(as.character(locationCrimes$long))
locationCrimes$lat <- as.numeric(as.character(locationCrimes$lat))
locationCrimes$frequency <- as.numeric(as.character(chicagoMVT$frequency))

## Plotting the location heatmap
#png(filename = "boston.png", width = 800, height = 600, units = "px")
map = ggmap(chicago) + geom_tile(data = chicagoMVT, aes(x = longitude, y = latitude, alpha = frequency), fill="dark green")
                           #fill = "red") + theme(axis.title.y = element_blank(), axis.title.x = element_blank())
#dev.off()
