# Generated by Django 3.2.7 on 2021-10-30 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0005_auto_20211028_0152'),
        ('court', '0002_remove_court_judge_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='judge_id',
            field=models.ManyToManyField(to='judge.Judge'),
        ),
    ]
