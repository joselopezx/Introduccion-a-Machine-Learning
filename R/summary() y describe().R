#install.packages('psych')
library('tidyverse')
library('psych')

csv<-'C:/Users/USER/Desktop/Codigos/R/introduccion a machine learning/melb_data.csv'
melbourne_data <- read_csv(csv)

summary(melbourne_data)

print('=======================================================================')

describe(melbourne_data)