# -*- coding:utf-8 -*-

import pandas as pd

# Read the file
data = pd.read_csv("../data/example.csv", low_memory=False)

# Output the number of rows
print("Total row:{0}".format(len(data)))

# See which headers are available
print(list(data))

accident_day = data[data.Day_of_Week == 1]
print("Accident which happend on a Sunday:{0}".format(len(accident_day)))

accident_sunday_twenty_cars = data[(data.Day_of_Week == 1) & (data.Number_of_Vehicles > 20)]
print("Accident which happend on Sunday involving > 20 cars: {0}".format(
    len(accident_sunday_twenty_cars)))



# Accidents in London on a Sunday
london_data = data[data['Police_Force'] == 1 & (data.Day_of_Week == 1)]
print("\nAccidents in London from 1979-2004 on a Sunday: {0}".format(
    len(london_data)))










































