# Generated by Django 3.2.7 on 2021-10-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ncase', '0002_alter_new_case_case_date'),
        ('police', '0004_police_new_case_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='police',
            name='case_id',
            field=models.ManyToManyField(to='Ncase.New_case'),
        ),
    ]
