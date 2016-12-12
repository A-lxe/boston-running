# Source: http://projects.flowingdata.com/tut/map-routes.R
library(plotKML)
library(rgdal)

# GPX files downloaded from MapMyRun
files <- paste("out", dir(path="out/"), "route.gpx", sep="/")
print(files)

# Consolidate routes in one drata frame
index <- c()
latitude <- c()
longitude <- c()
for (i in 1:length(files)) {
    print(paste(i, files[i]))
    route <- readOGR(files[i], "tracks")
    
    location <- coordinates(route)[[1]][[1]]
    
    index <- c(index, rep(i, dim(location)[1]))
    latitude <- c(latitude, location[,2])
    longitude <- c(longitude, location[,1])
}
routes <- data.frame(cbind(index, latitude, longitude))

# Map the routes
ids <- unique(index)
plot(routes$longitude, routes$latitude, type="n", axes=TRUE, xlab="", ylab="", main="", asp=1, ylim=c(42.330410,42.383941), xlim=c(-71.116591, -71.031704))
for (i in 1:length(ids)) {
	currRoute <- subset(routes, index==ids[i])
	lines(currRoute$longitude, currRoute$latitude, col="#00000020")
}
# Map the routes
ids <- unique(index)
plot(routes$longitude, routes$latitude, type="n", axes=TRUE, xlab="", ylab="", main="", asp=1, xlim=c( ylim=c(40,50))
for (i in 1:length(ids)) {
	currRoute <- subset(routes, index==ids[i])
	lines(currRoute$longitude, currRoute$latitude, col="#00000020")
}
