# NYC Taxi Fare Prediction

![alt text](http://www.taximac.com.ar/img/relojmuestra.jpg)

## Description

Data analysis for the [New York City Taxi Fare Prediction](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction). In this analysis we're only going to use 10,000 rows from the original dataset (~55,000,000 rows).

## Dataset

![alt text](http://i1376.photobucket.com/albums/ah11/mazzanicolas/Screen%20Shot%202018-08-14%20at%2010.20.58%20AM_zpsejfsp9ed.png?t=1534168182)

**pickup_datetime**   - `timestamp` value indicating when the taxi ride started.

**pickup_longitude**  - `float` for longitude coordinate of where the taxi ride started.

**pickup_latitude**   - `float` for latitude coordinate of where the taxi ride started.

**dropoff_longitude** - `float` for longitude coordinate of where the taxi ride ended.

**dropoff_latitude**  - `float` for latitude coordinate of where the taxi ride ended.

**passenger_count**   - `integer` indicating the number of passengers in the taxi ride.

## Removing unuseful columns

The **key** (unique identifier) column doesn't have any significant value so we're going to remove it. 

## Outlier data

Checking the diferent values for outlier rows.

