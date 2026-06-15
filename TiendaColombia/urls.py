"""
URL configuration for TiendaColombia project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.actores.urls')),
    path('', include('apps.categorias.urls')),
    path('', include('apps.gastos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
