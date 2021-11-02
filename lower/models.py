from django.db import models
from Ncase.models import New_case

Roll=(
    ('Defence','Defence '),
    ('Prosecutor','Prosecutor'),
)
class Lower(models.Model):

    case_id = models.ManyToManyField(New_case)
    lower_id = models.IntegerField(primary_key=True)
    lower_name = models.CharField(max_length=50)
    case_roll = models.CharField(choices=Roll,max_length=50,default='Defence')
    phone = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.lower_name
