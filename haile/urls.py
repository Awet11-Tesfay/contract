from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.contract_form, name='contract_form'),
    path('preview/<int:contract_id>/', views.contract_preview, name='contract_preview'),
    path('print/<int:contract_id>/', views.contract_print, name='contract_print'),
    path('delier/', views.delier_form, name='delier_form'),
    path('preview_delier/<int:delier_id>/', views.delier_preview, name='delier_preview'),
    path('print_delier/<int:delier_id>/', views.delier_print, name='delier_print'),

    path('deal/', views.deal_form, name='deal_form'),
    path('preview_deal/<int:deal_id>/', views.deal_preview, name='deal_preview'),
    path('print_deal/<int:deal_id>/', views.deal_print, name='deal_print'),


    path('consumer/', views.petroleum_form, name='petroleum_form'),
    path('preview_consumer/<int:petroleum_id>/', views.petroleum_preview, name='petroleum_preview'),
    path('print_consumer/<int:petroleum_id>', views.petroleum_print, name='petroleum_print'),
]
