from django.db import models

from judge.models import Judge
from Ncase.models import New_case
class Court(models.Model):

    case_id = models.ManyToManyField(New_case)
    judge_id = models.ManyToManyField(Judge)
    court_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    room_number = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField()
    def __str__(self):
        return self.court_name