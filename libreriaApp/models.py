from django.db import models

# Create your models here.
class Libros(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    editorial = models.CharField(max_length=200)
    fechadelanzamiento = models.CharField(max_length=50)
    autor= models.CharField(max_length=50)
    idioma= models.CharField(max_length=50)
    categoria= models.CharField(max_length=50)
    paginas = models.CharField(max_length=50)
    portada = models.CharField(max_length=50)

