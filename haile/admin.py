from django.contrib import admin
from .models import Contract, Delier, Deal

# Register your models here.
admin.site.register(Contract)
admin.site.register(Delier)
admin.site.register(Deal)
