from django.db import models
from django.contrib.auth.models import User

    
class Account(models.Model):
    user = models.OneToOneField(User,related_name="user_account_info",on_delete=models.CASCADE)
    security_code = models.CharField(max_length=6,null=True,blank=True)
    
    