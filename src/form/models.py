from django.db import models
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from uuid import uuid4


# Create your models here.


class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    x_created = CreationDateTimeField("x_created")
    x_modified = ModificationDateTimeField("x_modified")

    requester_name = models.CharField(max_length=64, verbose_name='Requester name', null=True, blank=True)
    sleepover_date_from = models.DateField(verbose_name='Sleepover date from', null=True, blank=True)
    sleepover_date_to = models.DateField(verbose_name='Sleepover date to', null=True, blank=True)
    num_persons = models.CharField(max_length=4, verbose_name='Number of persons', null=True, blank=True)
    accepted = models.BooleanField(default=False, verbose_name='Accepted')

    coitus = models.BooleanField(verbose_name='Is coitus', default=False)
    estimated_coitus_time_start = models.TimeField(null=True, blank=True, verbose_name='Estimated coitus time start')
    estimated_coitus_time_end = models.TimeField(null=True, blank=True, verbose_name='Estimated coitus time start')
