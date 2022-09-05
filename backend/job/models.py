from django.db import models




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