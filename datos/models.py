from django.db import models

class Familiar(models.Model):
  nombre = models.CharField(max_length=128)
  num_celular = models.IntegerField()
  fecha_nacimiento = models.DateField()