from django.urls import path
from . import views

app_name = 'response'

urlpatterns = [
    # post views
    path('responses/',views.responses, name='responses'),
    path('response/success/<int:id>/',views.success_responses, name='success_responses'),
    path('response/failed/<int:id>/',views.failed_responses, name='failed_responses'),
]