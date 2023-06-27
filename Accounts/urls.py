from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # post views
    path('', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
