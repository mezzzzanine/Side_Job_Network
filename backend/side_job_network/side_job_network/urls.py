from cgitb import handler
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from side_job_network import settings
from django.conf.urls.static import static

from side_job_network import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('newsroom/', include('newsroom.urls')),
]

handler404 = 'main.views.pageNotFound'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
