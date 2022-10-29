from django.contrib.gis.db import models
from collections import defaultdict

class Crime_Location_Detail(models.Model):
    crime_location_detail = models.TextField(unique=True)

    def __unicode__(self):
        return self.crime_location_detail

class CrimeType(models.Model):
    crime_description = models.TextField(unique=True)
    
    def __unicode__(self):
        return self.crime_description

class Resolution(models.Model):
    resolution = models.TextField(unique=True)

    def __unicode__(self):
        return self.resolution

class Crime(models.Model):
    api_id = models.BigIntegerField(primary_key=True, serialize=False)
    location = models.PointField()
    date = models.DateField()
    location_detail = models.ForeignKey(Crime_Location_Detail, on_delete=models.PROTECT)
    crime_type = models.ForeignKey(CrimeType, on_delete=models.PROTECT)
    resolution = models.ForeignKey(Resolution,default=1, on_delete=models.PROTECT)

    def calculate_crimeType_count(crimes):
        crime_groups = {}

        for crime in crimes:
            if not crime.crime_type.crime_description in crime_groups:
                crime_groups[crime.crime_type.crime_description] = 1
            else:
                crime_groups[crime.crime_type.crime_description] += 1
                
        group_groups_sorted = sorted(crime_groups.items(), key=lambda x: x[1], reverse=True)
        return group_groups_sorted
        
