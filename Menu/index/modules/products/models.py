from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    gramaje = models.PositiveIntegerField(help_text="mililitros")
    descripcion = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre