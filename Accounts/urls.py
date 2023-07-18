from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='auth/auth-signin.html',form_class=LoginForm), name='login'),
    path('profile/',check_company,name='profile'),
    path('acounts/new/',staff_account_creation,name='create_account'),
    path('accounts/',get_company_users,name='view_accounts'),
    path('security-code/<int:batch_id>/',verify_password,name='add_security_code'),
]