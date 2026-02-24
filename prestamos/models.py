from django.db import models
from usuarios.models import Estudiante
from libros.models import Libro

class Prestamo(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.estudiante} - {self.libro}"

