# Generated by Django 4.2.2 on 2023-08-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haile', '0014_alter_delier_map_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delier',
            name='ken',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='delier',
            name='wil_ken',
            field=models.CharField(default='', max_length=100),
        ),
    ]