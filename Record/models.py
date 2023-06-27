from django.db import models
from django.utils import timezone

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
    class RequestTypes(models.TextChoices):
        NEW = 'New','New'
        CHANGE = 'Change','Change'
        DELETE = 'Delete','Delete'
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE,related_name='batch_records')
    deduction_code = models.ForeignKey(DeductionCode,on_delete=models.DO_NOTHING,related_name='deduction_code_records')
    request_type = models.CharField(max_length=20,choices=RequestTypes.choices,default=RequestTypes.NEW)
    ec_number = models.CharField(max_length=8)
    id_number = models.CharField(max_length=11)
    transaction_refence = models.CharField(max_length=20)
    deductions_start_date = models.DateField()
    deductions_end_date = models.DateField()
    installment_amount = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    
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
    
    
    
    
