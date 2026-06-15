from django.contrib import admin
from .models import Gasto


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'monto', 'fecha', 'categoria', 'usuario')
    list_filter = ('categoria', 'fecha')
    search_fields = ('titulo', 'descripcion')
