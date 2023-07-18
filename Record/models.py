from django.db import models
from django.utils import timezone
import datetime
import random
from Batch.models import Batch,DeductionCode

class NewRequestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Record.RequestTypes.NEW)

class ChangeRequestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Record.RequestTypes.CHANGE)

class DeleteRequestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(status=Record.RequestTypes.DELETE)
                      
class Record(models.Model):
    class Status(models.TextChoices):
        CANCELED = 'CANCELED','CANCELED'
        DRAFT = 'DRAFT', 'DRAFT'
        FAILED = 'FAILED','FAILED'
        PROCESSED = 'PROCESSED', 'PROCESSED'
        PROCESSING = 'PROCESSING', 'PROCESSING'
        SUCCESS = 'SUCCESS', 'SUCCESS'
        SENT = 'SENT', 'SENT'
        SAVED = 'SAVED', 'SAVED'
    class RequestTypes(models.TextChoices):
        NEW = 'NEW','NEW'
        CHANGE = 'CHANGE','CHANGE'
        DELETE = 'DELETE','DELETE'
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,related_name='batch_records')
    deduction_code = models.ForeignKey(DeductionCode,on_delete=models.DO_NOTHING,related_name='deduction_code_records')
    record_id = models.CharField(max_length=20,null=True,blank=True)
    code = models.CharField(max_length=20,null=True,blank=True)
    status = models.CharField(max_length=15,choices=Status.choices,default=Status.DRAFT)
    request_type = models.CharField(max_length=20,choices=RequestTypes.choices,default=RequestTypes.NEW)
    ec_number = models.CharField(max_length=8)
    id_number = models.CharField(max_length=11)
    transaction_refence = models.CharField(max_length=20)
    deductions_start_date = models.DateField()
    record_source = models.CharField(max_length=20, default="Bulk Upload")
    deductions_end_date = models.DateField()
    installment_amount = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    # creator = models.ForeignKey()
    objects = models.Manager() # The default manager.
    new = NewRequestManager() # Our new request manager.
    change = ChangeRequestManager() # Our change request manager.
    delete = DeleteRequestManager() # Our delete request manager.
    
    class Meta:
        ordering = ['-date_created']
        indexes = [
            models.Index(fields=['-date_created']),
        ]

    def __str__(self):
        return self.transaction_refence
    
    def save(self, *args, **kwargs):
        # Get the count of existing Batch objects
        existing_count = Record.objects.count()
        # Get today's date
        today = datetime.datetime.today().date()
        date_str = str(today).replace("-","")
        # Generate the new batch_id by adding the today's date and count plus 1
        self.record_id = "REC" + date_str + str(random.randint(1000,10000))+ str(existing_count + 1)
        super(Record, self).save(*args, **kwargs)
    
 
class ResponseRecord(models.Model):
    pass   
    
