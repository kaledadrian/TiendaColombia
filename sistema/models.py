from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Actor(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('usuario', 'Usuario'),
    )
    
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    password = models.CharField(max_length=255, verbose_name="Contraseña")
    rol = models.CharField(max_length=20, choices=ROLES, default='usuario', verbose_name="Rol")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de registro")
    activo = models.BooleanField(default=True, verbose_name="Activo")
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def __str__(self):
        return f"{self.nombre} ({self.get_rol_display()})"
    
    class Meta:
        db_table = 'actores'

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

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50, unique=True, verbose_name="Método de pago")
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'metodos_pago'

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