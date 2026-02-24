from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    editorial = models.CharField(max_length=150)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.titulo
