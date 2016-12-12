library(ggplot2)
library(dplyr)
library(tidyr)
library(maps)
library(ggmap)

data <- read.csv('merge-heatmap.csv', stringsAsFactors = F)
data$runners <- log10(data$runners)
data$trees <- log10(data$trees)
data$pedestrians <- log10(data$pedestrians)

#data <- data %>% mutate(color = rgb(0, trees / 20, pedestrians / 13000))

boston <- get_map(location = 'Boston', zoom=13)
map = ggmap(boston) + geom_tile(data = data, aes(x = longitude, y = latitude, alpha = runners, fill = pedestrians)) + scale_fill_gradient(low = "green", high = "red")
