# Generated by Django 3.2.7 on 2021-10-22 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ncase', '0002_alter_new_case_case_date'),
        ('judge', '0002_delete_judge'),
    ]

    operations = [
        migrations.CreateModel(
            name='judge',
            fields=[
                ('judge_id', models.IntegerField(primary_key=True, serialize=False)),
                ('judge_name', models.CharField(max_length=50)),
                ('Court_name', models.CharField(max_length=50)),
                ('case_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ncase.new_case')),
            ],
        ),
    ]
