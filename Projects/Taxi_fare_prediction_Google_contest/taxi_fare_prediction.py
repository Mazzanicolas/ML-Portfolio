#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 09:53:56 2018

@author: Nicolás Mazza
"""
import matplotlib.pyplot      as plt
import pandas                 as pd
import numpy                  as np
from datetime import datetime as dt
from utils    import linear_distance, get_time_interval
from matplotlib.gridspec import GridSpec

#Loading Dataset
dataset = pd.read_csv('taxi_dataset_sample/taxi_dataset_sample.csv', nrows = 10000)
#Removing unuseful columns
dataset = dataset.drop('key', axis=1)
#Convert coords in to points
dataset['pickup_point']  = dataset[['pickup_latitude', 'pickup_longitude']].apply(
                                                lambda coords: (coords[0],coords[1]), axis=1)
dataset['dropoff_point'] = dataset[['dropoff_latitude', 'dropoff_longitude']].apply(
                                                lambda coords: (coords[0],coords[1]), axis=1)
#Remove coords
dataset = dataset.drop(['dropoff_longitude',
                        'dropoff_latitude' ,
                        'pickup_longitude' ,
                        'pickup_latitude'] , axis=1)
#Converting points in to linear distance
dataset['linear_distance'] = dataset[['pickup_point', 'dropoff_point']].apply(
                                                lambda coords: linear_distance(coords[0],coords[1]), axis=1)
#Remove points
dataset = dataset.drop(['pickup_point' ,
                        'dropoff_point',] , axis=1)
#Converting timestamps to dates
dataset['pickup_datetime'] = dataset['pickup_datetime'].apply(
                                                lambda date: dt.strptime(date[:19],'%Y-%m-%d %H:%M:%S'))
#Convert dates in to weekday, night, day, default (calcualted from other 3 to avoid dummy variable trap)
dataset['pickup_datetime'] = dataset['pickup_datetime'].apply(
                                                lambda date: get_time_interval(date))
#Split weekday, night and day in to columns
dataset['work_hour'] = dataset['pickup_datetime'].apply(
                                                lambda date: date[0])
dataset['night']     = dataset['pickup_datetime'].apply(
                                                lambda date: date[1])
dataset['day']       = dataset['pickup_datetime'].apply(
                                                lambda date: date[2])
#Remove date
dataset = dataset.drop(['pickup_datetime'], axis=1)
#Checking for outliers in the data
fare_amount     = dataset.fare_amount
passenger_count = dataset.passenger_count
linear_distance = dataset.linear_distance
plt.subplot(GridSpec(1, 3)[0, 0])
plt.boxplot(fare_amount)
plt.title('fare_amount')
plt.subplot(GridSpec(1, 3)[0, 1])
plt.boxplot(passenger_count)
plt.title('passenger_count')
plt.subplot(GridSpec(1, 3)[0, 2])
plt.boxplot(linear_distance)
plt.title('linear_distance')
plt.show()
#Getting fare_amount outliner values
fare_amount     = fare_amount[fare_amount < 22]
fare_amount     = fare_amount[fare_amount > 0]
#Getting passenger_count outliner values
passenger_count = passenger_count[passenger_count < 4]
passenger_count = passenger_count[passenger_count > 0]
#Getting linear_distance outliner values
linear_distance = linear_distance[linear_distance < 7800]
linear_distance = linear_distance[linear_distance > 0]
#Checking if outliners where removed succesfully
plt.subplot(GridSpec(1, 3)[0, 0])
plt.boxplot(fare_amount)
plt.title('fare_amount')
plt.subplot(GridSpec(1, 3)[0, 1])
plt.boxplot(passenger_count)
plt.title('passenger_count')
plt.subplot(GridSpec(1, 3)[0, 2])
plt.boxplot(linear_distance)
plt.title('linear_distance')
plt.show()
del fare_amount, passenger_count, linear_distance
#Applying changes to the dataset
#Removing fare_amount outliner values
dataset = dataset[dataset.fare_amount < 22]
dataset = dataset[dataset.fare_amount > 0]
#Removing passenger_count outliner values
dataset = dataset[dataset.passenger_count < 4]
dataset = dataset[dataset.passenger_count > 0]
#Removing linear_distance outliner values
dataset = dataset[dataset.linear_distance < 7800]
dataset = dataset[dataset.linear_distance > 0]