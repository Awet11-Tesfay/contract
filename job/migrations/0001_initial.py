# Generated by Django 4.2.2 on 2023-08-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.TextField()),
                ('starting_date', models.DateField(default='')),
            ],
        ),
    ]
