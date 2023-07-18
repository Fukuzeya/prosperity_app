from django.db import models
from django.utils import timezone
from Company.models import Company
# Create your models here.

class Invoice(models.Model):
    company = models.ForeignKey(Company, related_name='company_invoices',
                                on_delete=models.DO_NOTHING)
    invoice_number = models.CharField(max_length=20)
    
    
