from django.db import models

# Create your models here.

class Inventario(models.Model):
    Id = models.AutoField(primary_key=True)
    Grado=models.CharField(max_length=25)
    Materia=models.CharField(max_length=70)
    Nombre=models.CharField(max_length=70)
    Nom_archivo_ubi=models.CharField(max_length=70)
    Serie=models.CharField(max_length=70)
    Peso=models.CharField(max_length=15)
    Ubicacion=models.CharField(max_length=30)
    Ruta=models.CharField(max_length=70)

    def __str__(self):
        texto = "{0}-:({1} - {2})"
        return texto.format(self.Id, self.Nombre, self.Materia)
    