from django.db import models

# Create your models here.

class Invoice(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    date = models.CharField(primary_key=False, max_length=8)
    client = models.CharField(primary_key=False, max_length=100)
    dollar = models.FloatField()
    serial = models.CharField(primary_key=False, max_length=100)
    truck = models.CharField(primary_key=False, max_length=100)

    def __str__(self):
        return self.id