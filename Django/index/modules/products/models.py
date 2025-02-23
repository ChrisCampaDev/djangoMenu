from django.db import models

class Producto(models.Model):
    TYPE_CHOICES = [
        ('Lácteo', 'Lácteo'),
        ('Fruta', 'Fruta'),
        ('Verdura', 'Verdura'),
        ('Carne', 'Carne'),
        ('Bebida', 'Bebida'),
        ('Otro', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    gramaje = models.PositiveIntegerField(help_text="Peso en gramos")
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Otro')
    imagen = models.ImageField(upload_to='products/', blank=True, null=True, default='')

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"