from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
import uuid
# Create your models here.


class Company(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE','ACTIVE'
        SUSPENDED = 'SUSPENDED','SUSPENDED'
        DEACTIVATED = 'DEACTIVATED','DEACTIVATED'
    
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    company_ceo = models.CharField(max_length=100)
    physical_address = models.CharField(max_length=100)
    postal_address = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100,choices = Status.choices,default=Status.ACTIVE)
    
    def __str__(self): return self.name
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        
        
    def save(self, *args, **kwargs):
        Group.objects.get_or_create(name =self.name)
        super(Company, self).save(*args, **kwargs)
  