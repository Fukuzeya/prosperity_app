from django.contrib import admin

from Response.models import Response
# Register your models here.

@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['batch', 'recid','deductionCode','reference','amount','type','status','message']
    list_filter = ['batch','status','type','deductionCode']
    
    

