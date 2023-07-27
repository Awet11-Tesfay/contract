from django.db import models

class Contract(models.Model):
    companyname = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    address1 = models.CharField(max_length=100, default='')
    housenumber = models.CharField(max_length=20, default='')
    woreda = models.CharField(max_length=50, default='')
    kebele = models.CharField(max_length=50, default='')
    tell = models.CharField(max_length=20, default='')
    location = models.CharField(max_length=100, default='')
    location1 = models.CharField(max_length=100, default='')
    contract_date = models.DateField(null=True, blank=True)
    obliged_purchase = models.IntegerField(default=0)
    amount_litter = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    delivery_within = models.IntegerField(default=0)
    valid_year = models.IntegerField(default=0)
    pobox = models.IntegerField(default=0)
    supplierrepre_name = models.CharField(max_length=50, default='')
    supplierrepre_position = models.CharField(max_length=50, default='')
    supplierrepre_signe_date = models.DateField(null=True, blank=True)
    buyerrepre_name = models.CharField(max_length=50, default='')
    buyerrepre_position = models.CharField(max_length=50, default='')
    buyerrepre_signe_date = models.DateField(null=True, blank=True)
    signed_date = models.DateField(null=True, blank=True)
    wname = models.CharField(max_length=100, default='')
    waddress = models.CharField(max_length=50, default='')
    waddress1 = models.CharField(max_length=50, default='')
    wname1 = models.CharField(max_length=100, default='')
    suppliercname = models.CharField(max_length=100, default='')
    stown = models.CharField(max_length=100, default='')
    ssubcity = models.CharField(max_length=100, default='')
    sworeda = models.CharField(max_length=100, default='')
    stell = models.CharField(max_length=50, default='')
    sfax = models.IntegerField(default=0)
    shouse = models.CharField(max_length=50, default='')
    sroad = models.IntegerField(default=0)
    spobox = models.CharField(max_length=25, default='')



    def __str__(self):
        return self.companyname

class Delier(models.Model):
    ken = models.DateField(null=True, blank=True)
    sim = models.CharField(max_length=100, default='')
    sim1 = models.CharField(max_length=100, default='')
    yemiterut = models.CharField(max_length=100, default='')
    adrasha = models.CharField(max_length=100, default='')
    kilil = models.CharField(max_length=100, default='')
    zone = models.CharField(max_length=100, default='')
    woreda = models.CharField(max_length=100, default='')
    rsim = models.CharField(max_length=100, default='')
    rnumber = models.CharField(max_length=100, default='')
    rissued_date = models.DateField()
    radrasha = models.CharField(max_length=100, default='')
    wil_ken = models.DateField()

