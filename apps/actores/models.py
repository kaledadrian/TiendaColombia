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
