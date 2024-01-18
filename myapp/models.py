from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    file = models.FileField(upload_to='uploads')

    def __str__(self):
        return self.name
