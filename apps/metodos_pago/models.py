from django.db import models


class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Método de pago")
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'metodos_pago'
