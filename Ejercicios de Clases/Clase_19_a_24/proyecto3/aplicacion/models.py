from django.db import models
from django.contrib.auth.models import User

# Crear modelos aca
class Curso(models.Model):
    nombre = models.CharField(max_length=50) #Como max el nombre del curso denta 50 caracteres
    comision = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50, blank=False) #No acepta que este en blanco
    apellido = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    
    class Meta:
        ordering = ['apellido']
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ['apellido']
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()
    
    class Meta:
        ordering = ['nombre']
        
    def __str__(self):
        return f"{self.nombre}"

#Clase 24
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"