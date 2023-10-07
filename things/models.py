from django.db import models
from django.core import validators


class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=100, unique=False, blank=True)
    quantity = models.IntegerField(unique = False, validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)])
