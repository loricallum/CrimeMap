from datetime import datetime,date, timedelta
from .constants import EARTH_RADIUS_MILES
from math import atan2, acos, cos, sin, asin, radians, degrees

def get_month_intervals():
    startdate = date(2015,1,1)
    enddate =  date.today() - timedelta(30) #get previous month as last possible interval
    monthslist = []

    total_months = lambda dt: dt.month + 12 * dt.year

    for tot_m in range(total_months(startdate)-1, total_months(enddate)):
        year, month = divmod(tot_m, 12)
        monthslist.append(datetime(year, month+1, 1).strftime('%Y-%m'))

    monthslist.reverse()
    return monthslist

def get_month_intervals_as_tuple():
    return tuple((item, item) for item in get_month_intervals())

def add_miles_to_lat_lng(lat, lng, bearing, miles):
    latradian = radians(lat)
    lngradian = radians(lng)
    bearingradian = radians(bearing)

    lat2radians = asin(sin(latradian) * cos(miles/EARTH_RADIUS_MILES) + cos(latradian) * sin(miles/EARTH_RADIUS_MILES) * cos(bearingradian))
    lng2radians = lngradian + atan2(sin(bearingradian) * sin(miles/EARTH_RADIUS_MILES) * cos(latradian), cos(miles/EARTH_RADIUS_MILES) - sin(latradian) * sin(lat2radians))

    lat2degrees = degrees(lat2radians)
    lng2degrees = degrees(lng2radians)

    return (lat2degrees, lng2degrees)
