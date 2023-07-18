from django.urls import path
from . import views

app_name = 'record'

urlpatterns = [
    # post views
    path('', views.get_records, name='records'),
    path('new/',views.record_registration, name='new_record'),
    path('upload/',views.import_data, name='upload'),
    path('<str:record_id>/',views.record_detail, name='record_detail'),
    path('search/',views.filter_type, name='search'),
    path('search/status/',views.filter_status, name='search_status'),
]