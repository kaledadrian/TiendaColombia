from django.contrib import admin
from .models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'rol', 'activo', 'fecha_registro')
    list_filter = ('rol', 'activo')
    search_fields = ('nombre', 'email')
