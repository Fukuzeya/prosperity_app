from django.contrib import admin


admin.site.site_header ='PROSPERITY PARTNERS'
admin.site.site_title ='PROSPERITY | PARTNERS'
admin.site.index_title ='PROSPERITY PARTNERS'

from Company.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_ceo', 'physical_address',
                    'postal_address', 'town','status','date_joined']
    list_filter = ['town','status']
    
    fieldsets = (
        ('Company Information', {
            'fields': ('name', 'company_ceo'),
        }),
        ('Address Information', {
            'fields': ('physical_address', 'postal_address', 'email_address','town','country'),
        }),
    )