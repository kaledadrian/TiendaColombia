from django.db import models
from apps.categorias.models import Categoria
from apps.metodos_pago.models import MetodoPago
from apps.actores.models import Actor


class Gasto(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    monto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto (COP)")
    fecha = models.DateField(verbose_name="Fecha")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='gastos')
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True, blank=True)
    usuario = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='gastos')
    comprobante = models.ImageField(upload_to='comprobantes/', blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - ${self.monto:,.0f}"

    class Meta:
        db_table = 'gastos'
        ordering = ['-fecha', '-fecha_registro']
