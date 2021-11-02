from django.db import models
from Ncase.models import New_case
class Police(models.Model):
    case_id = models.ManyToManyField(New_case)
    police_id = models.IntegerField(primary_key=True)
    police_name = models.CharField(max_length=50)
    post_name = models.CharField(max_length=50)
    station_name = models.CharField(max_length=50)


