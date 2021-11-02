from django.db import models
from Ncase.models import New_case
class Judge(models.Model):
    case_id = models.ManyToManyField(New_case)
    judge_id = models.IntegerField(primary_key=True)
    judge_name = models.CharField(max_length=50)
    Court_name = models.CharField(max_length=50)

