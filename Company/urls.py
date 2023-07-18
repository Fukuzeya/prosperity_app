from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    # post views
    path('',views.get_companies, name='companies'),
    path('registration/', views.company_registration, name='company_registration'),
    path('dashboard/', views.company_dashboard, name='dashboard'),
]
