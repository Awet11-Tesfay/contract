# Generated by Django 4.2.2 on 2023-08-17 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haile', '0003_alter_contract_buyerrepre_signe_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petroleum',
            old_name='yewil_len',
            new_name='yewil_ken',
        ),
    ]