from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

import datetime

from Company.models import Company


class DeductionCode(models.Model):
    class Currency(models.TextChoices):
        USD = 'USD','USD'
        RTGS = 'RTGS','RTGS'
        RAND = 'RAND','RAND'
    
    class CurrencyCode(models.TextChoices):
        USD = '837472786','837472786'
        RTGS = '847373475','837373475'
        RAND = '853748262','853748262'
        
    deduction_code = models.CharField(max_length=250,unique=True)
    company = models.ForeignKey(Company,on_delete=models.DO_NOTHING,related_name='company_codes')
    currency = models.CharField(max_length=100,choices=Currency.choices)
    
    def save(self, *args, **kwargs):
        if self.currency == self.Currency.USD:
            self.deduction_code = self.CurrencyCode.USD + " - " + self.company.name + "(" + self.Currency.USD + ")"
        elif self.currency == self.Currency.RTGS:
            self.deduction_code = self.CurrencyCode.RTGS+ " - " + self.company.name + "(" + self.Currency.RTGS + ")"
        elif self.currency == self.Currency.RAND:
            self.deduction_code = self.CurrencyCode.RAND + " - " + self.company.name + "(" + self.Currency.RAND + ")"
            
        super(DeductionCode, self).save(*args, **kwargs)

class ProcessingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Batch.Status.PROCESSING)
                      
class ProcessedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Batch.Status.PROCESSED)
                      
class SentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Batch.Status.SENT)
                      
class PendingManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Batch.Status.PENDING)

class Batch(models.Model):
    class Status(models.TextChoices):
        SENT = 'Sent', 'Sent'
        PROCESSING = 'Processing', 'Processing'
        PROCESSED = 'Processed', 'ProcesSED'
        PENDING = 'Pending', 'Pending'
        
    batch_id = models.CharField(max_length=30,unique=True, db_index=True)
    deduction_code = models.ForeignKey(DeductionCode,on_delete=models.DO_NOTHING,related_name='deduction_code_batches')
    status = models.CharField(max_length=15,choices=Status.choices,default=Status.PENDING)
    paymaster = models.CharField(max_length=20,default='SSB')
    created_by = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='user_batches')
    date_created = models.DateTimeField(default=timezone.now)
    date_sent = models.DateTimeField(blank=True,null=True)
    
    def save(self, *args, **kwargs):
        # Get the count of existing Batch objects
        existing_count = Batch.objects.count()
        # Get today's date
        today = datetime.datetime.today().date()
        date_str = str(today).replace("-","")
        # Generate the new batch_id by adding the today's date and count plus 1
        self.batch_id = "ORD" + date_str + str(existing_count + 1)
        super(Batch, self).save(*args, **kwargs)

    objects = models.Manager() # The default manager.
    processing = ProcessingManager() # Our processing manager.
    processed = ProcessedManager() # Our processed manager.
    sent = SentManager() # Our sent manager.
    pending = PendingManager() # Our pending manager.

    class Meta:
        ordering = ['-date_created']
        indexes = [
            models.Index(fields=['-date_sent']),
        ]

    def __str__(self):
        return self.batch_id
