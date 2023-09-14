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
    contract_date = models.CharField(max_length=100, default='')
    obliged_purchase = models.CharField(max_length=100, default='')
    amount_litter = models.CharField(max_length=100, default='')
    delivery_within = models.CharField(max_length=100, default='')
    valid_year = models.CharField(max_length=100, default='')
    pobox = models.CharField(max_length=100, default='')
    supplierrepre_name = models.CharField(max_length=50, default='')
    supplierrepre_position = models.CharField(max_length=50, default='')
    supplierrepre_signe_date = models.CharField(max_length=100, default='')
    buyerrepre_name = models.CharField(max_length=50, default='')
    buyerrepre_position = models.CharField(max_length=50, default='')
    buyerrepre_signe_date = models.CharField(max_length=100, default='')
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
    sfax = models.CharField(max_length=100, default='')
    shouse = models.CharField(max_length=50, default='')
    sroad = models.CharField(max_length=100, default='')
    spobox = models.CharField(max_length=25, default='')



    def __str__(self):
        return self.companyname

class Delier(models.Model):
    ken = models.CharField(max_length=100, default='')
    sim = models.CharField(max_length=100, default='')
    yediler_kebele = models.CharField(max_length=100, default='')
    yediler_bet_kutur = models.CharField(max_length=100, default='')
    yediler_silk_kutr = models.CharField(max_length=100, default='')
    yediler_tewekay_kebele = models.CharField(max_length=100, default='')
    yedilier_tewekay_bet_kutr = models.CharField(max_length=100, default='')
    yediler_tewekay_silk_kutr = models.CharField(max_length=100, default='')
    madya_zone = models.CharField(max_length=100, default='')
    madya_wereda = models.CharField(max_length=100, default='')
    adrasha = models.CharField(max_length=100, default='')
    kilil = models.CharField(max_length=100, default='')
    zone = models.CharField(max_length=100, default='')
    woreda = models.CharField(max_length=100, default='')
    rsim = models.CharField(max_length=100, default='')
    rnumber = models.CharField(max_length=100, default='')
    rissued_date = models.CharField(max_length=100, default='')
    radrasha = models.CharField(max_length=100, default='')
    wil_ken = models.CharField(max_length=100, default='')
    madya_kilil = models.CharField(max_length=50, default='')
    madya_ketema = models.CharField(max_length=50, default='')
    madya_area = models.CharField(max_length=100, default='')
    map_kutr = models.CharField(max_length=100, default='')
    map_date = models.CharField(max_length=100, default='')
    ke_yetesete = models.CharField(max_length=500, default='')
    temezgbo_yemigegn = models.CharField(max_length=100, default='')
    misikir1_house_no = models.CharField(max_length=100, default=0)
    misikir2_house_no = models.CharField(max_length=100, default=0)
    miskir1 = models.CharField(max_length=100, default='')
    miskir2 = models.CharField(max_length=100, default='')
    misikir1_address = models.CharField(max_length=100, default='')
    misilir2_address = models.CharField(max_length=100, default='')
    kubanya_tewekay = models.CharField(max_length=100, default='')
    tewekay_position = models.CharField(max_length=100, default='')
    tewekay = models.CharField(max_length=100, default='')
    kubanya_position = models.CharField(max_length=100, default='')
    delier_tewekay = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.sim


class Deal(models.Model):
        ken = models.CharField(max_length=100, default='')
        sim = models.CharField(max_length=100, default='')
        madya_zone = models.CharField(max_length=100, default='')
        madya_wereda = models.CharField(max_length=100, default='')
        adrasha = models.CharField(max_length=100, default='')
        kilil = models.CharField(max_length=100, default='')
        zone = models.CharField(max_length=100, default='')
        woreda = models.CharField(max_length=100, default='')
        wil_ken = models.CharField(max_length=100, default='')
        madya_kilil = models.CharField(max_length=50, default='')
        madya_ketema = models.CharField(max_length=50, default='')
        madya_area = models.CharField(max_length=100, default='')
        map_kutr = models.CharField(max_length=100, default='')
        map_date = models.CharField(max_length=100, default='')
        ke_yetesete = models.CharField(max_length=500, default='')
        temezgbo_yemigegn = models.CharField(max_length=100, default='')
        misikir1_house_no = models.CharField(max_length=100, default=0)
        misikir2_house_no = models.CharField(max_length=100, default=0)
        miskir1 = models.CharField(max_length=100, default='')
        miskir2 = models.CharField(max_length=100, default='')
        misikir1_address = models.CharField(max_length=100, default='')
        misilir2_address = models.CharField(max_length=100, default='')
        kubanya_tewekay = models.CharField(max_length=100, default='')
        kubanya_position = models.CharField(max_length=100, default='')
        delier_tewekay = models.CharField(max_length=100, default='')
        yediler_kebele = models.CharField(max_length=100, default='')
        yediler_bet_kutur = models.CharField(max_length=100, default='')
        yediler_silk_kutr = models.CharField(max_length=100, default='')
        tewekay_position = models.CharField(max_length=100, default='')
        tewekay = models.CharField(max_length=100, default='')

        def __str__(self):
            return self.sim


class Petroleum(models.Model):
     yegezi_sim = models.CharField(max_length=100, default='')
     Addrasha = models.CharField(max_length=100, default='')
     Kilil = models.CharField(max_length=100, default='')
     ketema = models.CharField(max_length=100, default='')
     wereda = models.CharField(max_length=100, default='')
     kifle_letema = models.CharField(max_length=100, default='')
     kebele = models.CharField(max_length=100, default='')
     yebet_kutur = models.CharField(max_length=100, default='')
     silk_kutur = models.CharField(max_length=100, default='')
     gibir_meleya_kutur = models.CharField(max_length=100, default='')
     yefabrika_addrasha = models.CharField(max_length=100, default='')
     yewil_ken = models.CharField(max_length=100, default='')
     yemakrebya_gize = models.CharField(max_length=100, default='')
     ye_litter_bzat = models.CharField(max_length=100, default='')
     post_kutur = models.CharField(max_length=100, default='')
     yeakrabiw_tewekay = models.CharField(max_length=100, default='')
     yeakrabiw_tewekay_halafinet = models.CharField(max_length=100, default='')
     yegezi_tewekay = models.CharField(max_length=100, default='')
     yegezi_tewekay_halafinet = models.CharField(max_length=100, default='')

     andegna_misikir_sim = models.CharField(max_length=100, default='')
     andegna_lisikir_adrasha = models.CharField(max_length=100, default='')
     huletegna_misikir_sim = models.CharField(max_length=100, default='')
     huletegna_misikir_adrasha = models.CharField(max_length=100, default='')


class Transport(models.Model):
    wil_ken = models.CharField(max_length=40, default="")
    transporter_name = models.CharField(max_length=40, default="")
    title = models.CharField(max_length=20, default="")
    Adrasha = models.CharField(max_length=40, default="")
    ketema = models.CharField(max_length=40, default="")
    kifle_ketema = models.CharField(max_length=40, default="")
    wereda = models.CharField(max_length=40, default="")
    yebet_kutr = models.CharField(max_length=40, default="")
    silk_kutr = models.CharField(max_length=40, default="")
    date_year = models.CharField(max_length=40, default="")
    yekubanya_tewekay = models.CharField(max_length=40, default="")
    yekubanya_tewekay_position = models.CharField(max_length=40, default="")
    transporter_tewekay = models.CharField(max_length=40, default="")
    transporter_tewekay_position = models.CharField(max_length=40, default="")
    miskir1 = models.CharField(max_length=40, default="")
    miskir2 = models.CharField(max_length=40, default="")
    misikir1_address = models.CharField(max_length=40, default="")
    misikir2_address = models.CharField(max_length=40, default="")
    misikir1_house_no = models.CharField(max_length=40, default="")
    misikir2_house_no = models.CharField(max_length=40, default="")
    yekubanya_title = models.CharField(max_length=40, default="")
    contract_length = models.CharField(max_length=40, blank=True, default="")
    numberof_cars = models.CharField(max_length=80, default="")
    yeseleda_kutr = models.CharField(blank=False, default="")
    yetesabi_kutr = models.CharField(blank=False, default="")
    yeseleda_kutr1 = models.CharField(blank=False, default="")
    yetesabi_kutr1 = models.CharField(blank=False, default="")
    yeseleda_kutr2 = models.CharField(blank=False, default="")
    yetesabi_kutr2 = models.CharField(blank=False, default="")
    yeseleda_kutr3 = models.CharField(blank=False, default="")
    yetesabi_kutr3 = models.CharField(blank=False, default="")
    wname = models.CharField(max_length=40, default="")
    wname1 = models.CharField(max_length=40, default="")
    waddress = models.CharField(max_length=40, default="")
    waddress1 = models.CharField(max_length=40, default="")







     