from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Accounts.urls',namespace='accounts')),
    path('batch/', include('Batch.urls', namespace='batch')),
    path('company/', include('Company.urls', namespace='company')),
    # path('record/', include('Record.urls', namespace='record')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

