# Generated by Django 3.2.7 on 2021-10-22 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ncase', '0002_alter_new_case_case_date'),
        ('police', '0006_remove_police_case_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='police',
            name='New_case_id',
            field=models.ForeignKey(default='loding', on_delete=django.db.models.deletion.CASCADE, to='Ncase.new_case'),
        ),
    ]