from django.db import models

# Create your models here.
from Ncase.models import New_case
case_status=(
    ('Solve','Solve'),
    ('Ranning','Ranning'),
    ('Dismiss','Dismiss'),
)
class Status(models.Model):
    case_id = models.ForeignKey(New_case, on_delete=models.CASCADE)
    status = models.CharField(choices=case_status,max_length=50)
    def __str__(self):
        return self.status