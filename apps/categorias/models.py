from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    color = models.CharField(max_length=7, default='#007bff', verbose_name="Color")
    icono = models.CharField(max_length=50, default='bi-tag', verbose_name="Icono")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categorias'
