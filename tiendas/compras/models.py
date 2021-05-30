from django.db import models
from django.utils import timezone

class Registro(models.Model):
    centro_comercial = models.IntegerField(default = 1)
    distancia_comercial = models.IntegerField(default = 10)
    centro_comercial_visitado = models.IntegerField(default = 1)

    

