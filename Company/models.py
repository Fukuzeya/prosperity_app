from django.db import models
from django.utils import timezone
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=250)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self): return self.name
