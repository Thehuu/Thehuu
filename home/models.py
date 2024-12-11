from django.db import models

class ReliefLocation(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='relief_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class AccidentLocation(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='accident_images/', blank=True, null=True)

    def __str__(self):
        return self.name
