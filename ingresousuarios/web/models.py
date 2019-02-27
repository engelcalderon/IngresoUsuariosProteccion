from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=80)
    correo_electronico = models.CharField(max_length=254, unique=True)
    contrasena = models.TextField()