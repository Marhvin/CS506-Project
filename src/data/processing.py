""" 
Pre-processing data for mbta and weather

1. Merge all data entries by their dates and station name
2. Possibly combine the data of weather and the mbta, ie. entry with how the
  weather is like on that date
  
  
1. Handle missing values or inconsistencies.
2. Align the dates in both datasets to ensure each weather record matches a corresponding gate entry day.
    Entries for precipitation , temperature,
3. Organize stations by MBTA line, if necessary.

"""
import pandas as pd
import numpy as np
import os

df_mbta = pd.read_csv('CS506-Project/data/raw/mbta_data.csv')
print("Head of MBTA data: \n", df_mbta.head())

print("Null values of MBTA data: \n", df_mbta.isnull().sum())

"""

  Output of null values:

  service_date          0
  time_period           0
  stop_id          129968
  station_name          0
  route_or_line         0
  gated_entries         0
  ObjectId              0


  Since stop_id is just another identifier of the unique stops, 
  it is okay to drop it and just use station_name, which has no 
  missing vlaues.

  Some routes/lines also share the same station, and since our
  goal is to look at the station as a whole, it should be okay to
  drop the route_or_line column. 

  Later on, the entries with the same service_date and station_name
  will merged to get the entries number of the station for that whole day.

"""


"""Dropping stop_id"""
df_mbta = df_mbta.drop(columns=['stop_id', 'route_or_line'])
print("Remaining columns of MBTA data: \n", df_mbta.columns)

"""
  Going through the weathers data set and finding null values
  
  Finding the important weather values and keeping them
    Then merge with the mbta dataset by the date to create a new dataset
"""

df_weather = pd.read_csv('CS506-Project/data/raw/weather_data.csv')
print("Head of weather data: \n", df_weather.head())