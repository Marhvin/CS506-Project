# CS506 Project Proposal

## Project Description
Using historical data publicly available from the MBTA website, our project will predict the number of people that use the train of a given station (By measuring gate entries), depending on the weather conditions (Temp., Clear, Rain, Snow). 

## Goals
The goal of this project is to successfully predict the number of gate entries into MBTA train stations based on weather conditions. This will help MBTA planners understand how weather affects day-to-day ridership in order to improve operational logistics, such as scheduling train arrivals/departures, staffing, and more.

## Data Collection
- The number of gate entries for each MBTA train station per day in 2018-2023. This data can be sourced from MassGIS Data Hub, which publicly provides data on MBTA gate entries per day. 
- Weather conditions/report per day in 2018-2023, which can be sourced from a Kaggle dataset, which provides the temperature, precipitation, condition, humidity, and wind for a given day. (https://www.kaggle.com/datasets/swaroopmeher/boston-weather-2013-2023)

## Data Cleaning
- Organize stations by line, being able to get number of entries per line
- Aliign dates of data together, making sure each time period corresponds with eachother

## Modelling
- Use a linear regression model to determine the correlation between different weather variables and ridership.


## Visualization
- Time Series Plots to compare ridership between lines
- Scatter Plots with Regression Lines (Ridership vs. Temperature, Precipitation, Wind Speed)
- Interactive map of MBTA stations showing ridership in different weather conditions


## Test Plan / Metrics

Train on Past Data, Test on Future Data 
- Train on: Data from 2018 to 2022 
- Test on: Data from 2023

