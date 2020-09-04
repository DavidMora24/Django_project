from django.db import models

class product(models.Model):

    name = models.CharField(max_length=12)
    cantidad = models.CharField(max_length=12)
