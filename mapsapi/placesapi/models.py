from django.db import models

class Place(models.Model):
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)
    desc = models.CharField(max_length=1024)
    image = models.BinaryField()

