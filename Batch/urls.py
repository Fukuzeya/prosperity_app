from django.urls import path
from .admin import prosperity_admin_site
from . import views

app_name = 'batch'

urlpatterns = [
    # post views
    path('',views.all_batches, name='batches'),
    path('drafts/',views.draft_batches, name='drafts'),
    path('codes/', views.get_deduction_codes, name='codes'),
    path('codes/new/',views.deduction_code_registration, name='code_registration'),
    path('send/batch/',views.send_batch, name='send_batch'),
    path('<int:id>/upload_excel/', views.upload_responses, name='upload_excel'),
    path('<int:id>/',views.view_batch, name='view_batch'),
]