from police_api import constants
from datetime import datetime
import requests
from django.contrib.gis.geos import Point
import logging

from common.models import Crime, CrimeType, Crime_Location_Detail, Resolution

logger = logging.getLogger(__name__)

def get_all_crimes(lat, lng, date):
    dateFormatted = datetime.strptime(date, "%Y-%m")
    params = {'lat': lat, 'lng': lng, 'date': date }

    return basic_all_crime_api(params)

def get_crimes_within_area(areaPolygon, date):
    dateFormatted = datetime.strptime(date, "%Y-%m")
    params = {'poly': areaPolygon, 'date': date }

    return basic_all_crime_api(params)

def basic_all_crime_api(params):
    apiurl = constants.BASE_POLICE_API_URL + constants.STREET_CRIME_URL + constants.ALL_CRIME_URL
    apirequest = requests.get(apiurl, params=params)
    logger.info(f"police api request: ({apirequest.status_code}) {apirequest.reason}")

    if apirequest.status_code == 200:
        crimes = apirequest.json()
        return crimes
    else:
        return ()


def save_crimes_JSON(crimesJSON):
    crimesformatted = []
    logger.info(f"Attempting to save {len(crimesJSON)} crimes")

    for crime in crimesJSON:
        resolution = Resolution.objects.get(id=1)

        crimePoint = Point(float(crime['location']['longitude']),float(crime['location']['latitude']))

        crimeType, crimetype_created = CrimeType.objects.get_or_create(crime_description=crime['category']) 

        if crime['outcome_status'] and crime['outcome_status']['category']:
                resolutiontext = crime['outcome_status']['category']
                resolution, resolution_created = Resolution.objects.get_or_create(resolution=resolutiontext)

        crimelocationdetail, locdetail_created = Crime_Location_Detail.objects.get_or_create(crime_location_detail=crime['location']['street']['name'])

        crimesformatted.append(Crime(api_id=crime['id'],
                               location=crimePoint,
                               date=datetime.strptime(crime['month'],'%Y-%m'),
                               location_detail=crimelocationdetail, 
                               crime_type=crimeType,
                               resolution=resolution))
                           
    Crime.objects.bulk_create(crimesformatted, ignore_conflicts=True)
    logger.info(f"Saved {len(crimesformatted)} crimes")

    return crimesformatted