# Generated by Django 4.2.2 on 2023-08-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('address1', models.CharField(default='', max_length=100)),
                ('housenumber', models.CharField(default='', max_length=20)),
                ('woreda', models.CharField(default='', max_length=50)),
                ('kebele', models.CharField(default='', max_length=50)),
                ('tell', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=100)),
                ('location1', models.CharField(default='', max_length=100)),
                ('contract_date', models.DateField(blank=True, null=True)),
                ('obliged_purchase', models.IntegerField(default=0)),
                ('amount_litter', models.DecimalField(decimal_places=10, max_digits=20, null=True)),
                ('delivery_within', models.IntegerField(default=0)),
                ('valid_year', models.IntegerField(default=0)),
                ('pobox', models.IntegerField(default=0)),
                ('supplierrepre_name', models.CharField(default='', max_length=50)),
                ('supplierrepre_position', models.CharField(default='', max_length=50)),
                ('supplierrepre_signe_date', models.DateField(blank=True, null=True)),
                ('buyerrepre_name', models.CharField(default='', max_length=50)),
                ('buyerrepre_position', models.CharField(default='', max_length=50)),
                ('buyerrepre_signe_date', models.DateField(blank=True, null=True)),
                ('signed_date', models.DateField(blank=True, null=True)),
                ('wname', models.CharField(default='', max_length=100)),
                ('waddress', models.CharField(default='', max_length=50)),
                ('waddress1', models.CharField(default='', max_length=50)),
                ('wname1', models.CharField(default='', max_length=100)),
                ('suppliercname', models.CharField(default='', max_length=100)),
                ('stown', models.CharField(default='', max_length=100)),
                ('ssubcity', models.CharField(default='', max_length=100)),
                ('sworeda', models.CharField(default='', max_length=100)),
                ('stell', models.CharField(default='', max_length=50)),
                ('sfax', models.IntegerField(default=0)),
                ('shouse', models.CharField(default='', max_length=50)),
                ('sroad', models.IntegerField(default=0)),
                ('spobox', models.CharField(default='', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ken', models.CharField(default='', max_length=100)),
                ('sim', models.CharField(default='', max_length=100)),
                ('madya_zone', models.CharField(default='', max_length=100)),
                ('madya_wereda', models.CharField(default='', max_length=100)),
                ('adrasha', models.CharField(default='', max_length=100)),
                ('kilil', models.CharField(default='', max_length=100)),
                ('zone', models.CharField(default='', max_length=100)),
                ('woreda', models.CharField(default='', max_length=100)),
                ('wil_ken', models.CharField(default='', max_length=100)),
                ('madya_kilil', models.CharField(default='', max_length=50)),
                ('madya_ketema', models.CharField(default='', max_length=50)),
                ('madya_area', models.CharField(default='', max_length=100)),
                ('map_kutr', models.CharField(default='', max_length=100)),
                ('map_date', models.CharField(default='', max_length=100)),
                ('ke_yetesete', models.CharField(default='', max_length=500)),
                ('temezgbo_yemigegn', models.CharField(default='', max_length=100)),
                ('misikir1_house_no', models.IntegerField(default=0)),
                ('misikir2_house_no', models.IntegerField(default=0)),
                ('miskir1', models.CharField(default='', max_length=100)),
                ('miskir2', models.CharField(default='', max_length=100)),
                ('misikir1_address', models.CharField(default='', max_length=100)),
                ('misilir2_address', models.CharField(default='', max_length=100)),
                ('kubanya_tewekay', models.CharField(default='', max_length=100)),
                ('kubanya_position', models.CharField(default='', max_length=100)),
                ('delier_tewekay', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Delier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ken', models.CharField(default='', max_length=100)),
                ('sim', models.CharField(default='', max_length=100)),
                ('yediler_kebele', models.CharField(default='', max_length=100)),
                ('yediler_bet_kutur', models.CharField(default='', max_length=100)),
                ('yediler_silk_kutr', models.CharField(default='', max_length=100)),
                ('yediler_tewekay_kebele', models.CharField(default='', max_length=100)),
                ('yedilier_tewekay_bet_kutr', models.CharField(default='', max_length=100)),
                ('yediler_tewekay_silk_kutr', models.CharField(default='', max_length=100)),
                ('madya_zone', models.CharField(default='', max_length=100)),
                ('madya_wereda', models.CharField(default='', max_length=100)),
                ('adrasha', models.CharField(default='', max_length=100)),
                ('kilil', models.CharField(default='', max_length=100)),
                ('zone', models.CharField(default='', max_length=100)),
                ('woreda', models.CharField(default='', max_length=100)),
                ('rsim', models.CharField(default='', max_length=100)),
                ('rnumber', models.CharField(default='', max_length=100)),
                ('rissued_date', models.CharField(default='', max_length=100)),
                ('radrasha', models.CharField(default='', max_length=100)),
                ('wil_ken', models.CharField(default='', max_length=100)),
                ('madya_kilil', models.CharField(default='', max_length=50)),
                ('madya_ketema', models.CharField(default='', max_length=50)),
                ('madya_area', models.CharField(default='', max_length=100)),
                ('map_kutr', models.CharField(default='', max_length=100)),
                ('map_date', models.CharField(default='', max_length=100)),
                ('ke_yetesete', models.CharField(default='', max_length=500)),
                ('temezgbo_yemigegn', models.CharField(default='', max_length=100)),
                ('misikir1_house_no', models.IntegerField(default=0)),
                ('misikir2_house_no', models.IntegerField(default=0)),
                ('miskir1', models.CharField(default='', max_length=100)),
                ('miskir2', models.CharField(default='', max_length=100)),
                ('misikir1_address', models.CharField(default='', max_length=100)),
                ('misilir2_address', models.CharField(default='', max_length=100)),
                ('kubanya_tewekay', models.CharField(default='', max_length=100)),
                ('tewekay_position', models.CharField(default='', max_length=100)),
                ('tewekay', models.CharField(default='', max_length=100)),
                ('kubanya_position', models.CharField(default='', max_length=100)),
                ('delier_tewekay', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Petroleum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yegezi_sim', models.CharField(default='', max_length=100)),
                ('Addrasha', models.CharField(default='', max_length=100)),
                ('Kilil', models.CharField(default='', max_length=100)),
                ('ketema', models.CharField(default='', max_length=100)),
                ('wereda', models.CharField(default='', max_length=100)),
                ('kifle_letema', models.CharField(default='', max_length=100)),
                ('kebele', models.CharField(default='', max_length=100)),
                ('yebet_kutur', models.CharField(default='', max_length=100)),
                ('silk_kutur', models.CharField(default='', max_length=100)),
                ('gibir_meleya_kutur', models.CharField(default='', max_length=100)),
                ('yefabrika_addrasha', models.CharField(default='', max_length=100)),
                ('yewil_len', models.CharField(default='', max_length=100)),
                ('yemakrebya_gize', models.CharField(default='', max_length=100)),
                ('ye_litter_bzat', models.CharField(default='', max_length=100)),
                ('post_kutur', models.CharField(default='', max_length=100)),
                ('yeakrabiw_tewekay', models.CharField(default='', max_length=100)),
                ('yeakrabiw_tewekay_halafinet', models.CharField(default='', max_length=100)),
                ('yegezi_tewekay', models.CharField(default='', max_length=100)),
                ('yegezi_tewekay_halafinet', models.CharField(default='', max_length=100)),
                ('andegna_misikir_sim', models.CharField(default='', max_length=100)),
                ('andegna_lisikir_adrasha', models.CharField(default='', max_length=100)),
                ('huletegna_misikir_sim', models.CharField(default='', max_length=100)),
                ('huletegna_misikir_adrasha', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
