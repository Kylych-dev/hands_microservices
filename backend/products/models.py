from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass