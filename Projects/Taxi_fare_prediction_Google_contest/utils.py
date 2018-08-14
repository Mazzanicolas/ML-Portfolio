# -*- coding: utf-8 -*-
import math as m
def linear_distance(pickup_point, dropoff_point):
    lat1, lon1 = pickup_point
    lat2, lon2 = dropoff_point
    r = 6371e3;
    φ1 = m.radians(lat1)
    φ2 = m.radians(lat2)
    Δφ = m.radians(lat2-lat1)
    Δλ = m.radians(lon2-lon1)
    a = m.sin(Δφ/2) * m.sin(Δφ/2) + m.cos(φ1) * m.cos(φ2) * m.sin(Δλ/2) * m.sin(Δλ/2)
    c = 2 * m.atan2(m.sqrt(a), m.sqrt(1-a))
    d = r * c
    return d

def get_time_interval(date):
    work_hour = is_weekday_work_hour(date)
    night     = is_night(date)
    day       = is_day(date)
    return (work_hour, night, day)

def is_night(date):
    if date.hour > 19 and date.hour < 7:
        return 1
    return 0

def is_day(date):
    if date.hour > 5 and date.hour < 17:
        return 1
    return 0

def is_weekday_work_hour(date):
    if date.isoweekday() > 0 and date.isoweekday() < 5:
        if date.hour > 15 and date.hour < 21:
            return 1
    return 0