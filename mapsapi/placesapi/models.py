from django.db import models

class Place(models.Model):
    lat = models.DecimalField(max_digits=23, decimal_places=20)
    lng = models.DecimalField(max_digits=23, decimal_places=20)
    desc = models.CharField(max_length=1024)
    name = models.CharField(max_length=50)

