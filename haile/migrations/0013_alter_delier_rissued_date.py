# Generated by Django 4.2.2 on 2023-08-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haile', '0012_alter_delier_ke_yetesete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delier',
            name='rissued_date',
            field=models.CharField(default='', max_length=100),
        ),
    ]
