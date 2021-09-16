from django.db import models
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from uuid import uuid4


# Create your models here.


class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    x_created = CreationDateTimeField("x_created")
    x_modified = ModificationDateTimeField("x_modified")

    requester_name = models.CharField(max_length=64, verbose_name='Requester name')
    sleepover_date_from = models.DateField(verbose_name='Sleepover date from')
    sleepover_date_to = models.DateField(verbose_name='Sleepover date to')
    num_persons = models.IntegerField(verbose_name='Number of persons')
    accepted = models.BooleanField(default=False, verbose_name='Accepted')

    coitus = models.BooleanField(verbose_name='Is coitus')
    estimated_coitus_time = models.BooleanField(null=True, blank=True)
