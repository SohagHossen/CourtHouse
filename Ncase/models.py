from django.db import models

class New_case(models.Model):

    case_id=models.IntegerField(primary_key=True,auto_created=(00))
    case_name  = models.CharField(max_length=50)
    prose_name  = models.CharField(max_length=50)
    def_name = models.CharField(max_length=50)
    case_date = models.DateField()



