# Generated by Django 3.2.7 on 2021-10-22 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0003_judge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='judge',
            old_name='case_id',
            new_name='case',
        ),
    ]