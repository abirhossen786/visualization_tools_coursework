# Visualizations
library(hrbrthemes)
library(gganimate)
library(gapminder)
library(babynames)
library(ggthemes)
library(cowplot)
library(ggplot2)

# Data Manipulation
library(dplyr)

# Statistics
library(DescTools)

# Loading the database 
data <- read.csv("/vgsales.csv", stringsAsFactors = FALSE)

# Removing the Rank column
data$Rank <- NULL

# Filtering only the records of interest for this study, removing the records with Year = NaN and records with the year above 2016
data <- data[data$Year != "N/A" & data$Year != "2017" & data$Year != "2020", ]
data$Year <- factor(data$Year)

# Viewing the first 6 DataFrame records
head(data, 6)

summary(data)

df_global <- aggregate(list(Global_Sales = data$Global_Sales), list(Year = data$Year), sum)
df_global <- df_global[order(df_global$Global_Sales), ]

a <- c()

for(i in 1:nrow(df_global)){
    a <- c(a, i)
}

row.names(df_global) <- a
df_global

options(repr.plot.width = 20, repr.plot.height = 11)


a <- ggplot(data = df_global, mapping = aes(x = Year, y = Global_Sales)) +
         geom_segment(aes(xend=Year, yend=0, color = Year), size = 2.3, alpha = .8) +
         geom_point(mapping = aes(fill = Year), size = 5, shape = 21) +
         geom_line(group = 1, size = 1.1, linetype = 10, color = "red") +
         xlab("Year") +
         ylab("Global Sales") +
         theme_classic() +
         theme(plot.title = element_text(size = 25, face = "bold", hjust = .5),
               axis.title.x = element_text(size = 22, hjust = .5),
               axis.title.y = element_text(size = 22, hjust = .5),
               axis.text.x = element_text(size = 15),
               axis.text.y = element_text(size = 20, face = "bold"),
               legend.position = "none")


plot_grid(a)
