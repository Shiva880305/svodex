# svodex_web/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('o-nas/', views.about, name='about'),
    path('kontakty/', views.contact, name='contact'),
    path('reference/', include('reference.urls')),
    path('nabidka-sluzeb/', views.service_list, name='service_list'),
    path('certifikaty/', views.certificate_list, name='certificate_list'),
    path('nabidka-sluzeb/<int:pk>/', views.service_detail, name='service_detail'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
