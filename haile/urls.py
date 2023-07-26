from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.contract_form, name='contract_form'),
    path('preview/<int:contract_id>/', views.contract_preview, name='contract_preview'),
    path('print/<int:contract_id>/', views.contract_print, name='contract_print'),
    path('delier/', views.delier_form, name='delier_form'),
    path('preview/<int:delier_id>/', views.delier_preview, name='delier_preview'),
    path('print/<int:delier_id>/', views.delier_print, name='delier_print'),
]
