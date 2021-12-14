from django.db import models

class Element(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, null=True)
    ecoPoints = models.FloatField()

