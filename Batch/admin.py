from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.admin import AdminSite

class ProsperityPartnersAdminSite(AdminSite):
    site_header = 'Prosperity Partners'
    
prosperity_admin_site = ProsperityPartnersAdminSite(name='prosperity_admin')



from Batch.models import Batch, DeductionCode

admin.site.register(DeductionCode)

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ['batch_id', 'deduction_code',
                    'company','status','date_created']
    list_filter = ['company','date_created','status']
    
    actions = ['upload_excel']

    def upload_excel(self, request, queryset):
        selected = queryset.count()
        if selected == 1:
            id = queryset.first().id
            url = reverse('batch:upload_excel', args=[id])
            return HttpResponseRedirect(url)
        else:
            self.message_user(request, "Please select only one batch.")
