# Generated by Django 4.2.2 on 2023-08-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haile', '0010_delier_yediler_silk_kutr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delier',
            name='madya_wereda',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='delier',
            name='madya_zone',
            field=models.CharField(default='', max_length=100),
        ),
    ]