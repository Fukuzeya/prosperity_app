from django.urls import path
from . import views

app_name = 'batch'

urlpatterns = [
    # post views
    path('codes/', views.get_deduction_codes, name='codes'),
    path('codes/new/',views.deduction_code_registration, name='code_registration'),
]