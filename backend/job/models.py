from django.db import models


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
        max_length=10,
        choices=Industry.choices,
        default=Industry.IT
    )
    experiance = models.CharField(
        max_length=10,
        choices=Experiance.choices,
        default=Experiance.NO_EXPERIANCE
    )