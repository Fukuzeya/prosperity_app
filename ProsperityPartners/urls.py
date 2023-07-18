from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Accounts.urls',namespace='accounts')),
    path('batches/', include('Batch.urls', namespace='batch')),
    path('companies/', include('Company.urls', namespace='company')),
    path('records/', include('Record.urls', namespace='record')),
    path('responses/', include('Response.urls', namespace='response')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
#django-insecure-m0s&i_6&kcp39hv53*g$=64e6#ppb&efdxm!krv!l7_#q%w&a$

