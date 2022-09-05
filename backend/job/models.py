from django.db import models
from django.core.validators import MinValueValidators, MaxValueValidators
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import PointField
from datetime import *
from django.contrib.auth.models import User


import geocoder
import os

class JobType(models.TextChoices):
    Permanent = 'Permanent'
    Temporary = 'Temporary'
    Intership = 'Intership'


class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    PhD = 'PhD'


class Industry(models.TextChoices):
    Busniess = 'Busniess'
    Banking = 'Banking'
    Education = 'Education/Training'
    Telecommunication = 'Telecommunication'
    IT = 'Information Technology'


class Experiance(models.TextChoices):
    NO_EXPERIANCE='No Experiance'
    ONE_YEAR='1 Year'
    TWO_YEAR= '2 Years'
    THREE_YEAR_PLUS=' 3 Years and above'


# Making Last Date To Apply To Minimum 10 Days
def return_date_time():
    now = datetime.now()
    return now + timedelta(days=10)



class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=100, null=True)
    job_type= models.CharField(
        max_length=10,
        choices=JobType.choices,
        default=JobType.Permanent
    )
    education= models.CharField(
        max_length=10,
        choices=Education.choices,
        default=Education.Bachelors
    )
    industry= models.CharField(
        max_length=30,
        choices=Industry.choices,
        default=Industry.IT
    )
    experiance = models.CharField(
        max_length=20,
        choices=Experiance.choices,
        default=Experiance.NO_EXPERIANCE
    )
    salary = models.IntegerField(default=1, validators=[MinValueValidators(1), MaxValueValidators(1000000)])
    positions = models.IntegerField(default=1)
    company = models.CharField(max_length=100, null=True)
    point = gismodels.PointField(default=Point(0.0,0.0))
    lastDate = models.DateTimeField(default=return_date_time)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        g = geocoder.mapquest(self.address, key=os.eviron.get('GEOCODER_API'))
        lng = g.lng
        lat = g.lat

        
        self.point= Point(lng, lat)
        super(Job, self).save(*args, **kwargs)



