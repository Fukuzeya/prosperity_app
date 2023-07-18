from django.db import models

from Batch.models import Batch
# Create your models here.


class Response(models.Model):
    batch = models.ForeignKey(Batch,on_delete=models.DO_NOTHING,related_name='responses')
    recid = models.CharField(max_length=10,null=True,blank=True)
    deductionCode = models.CharField(max_length=100,null=True,blank=True)
    reference = models.CharField(max_length=100,null=True,blank=True)
    idNumber = models.CharField(max_length=15,null=True,blank=True)
    ecNumber = models.CharField(max_length=9,null=True,blank=True)
    type = models.CharField(max_length=10,null=True,blank=True)
    status = models.CharField(max_length=10,null=True,blank=True)
    startDate = models.CharField(max_length=100,null=True,blank=True)
    endDate = models.CharField(max_length=100,null=True,blank=True)
    amount = models.DecimalField(decimal_places=2,max_digits=10)
    name = models.CharField(max_length=100,null=True,blank=True)
    bankAccount  = models.CharField(max_length=100,null=True,blank=True)
    message = models.CharField(max_length=100,null=True,blank=True)