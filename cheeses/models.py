from django.db import models
# name: String
# origin_country: String
# type: String
# Create your models here.
class Cheese(models.Model):
    name = models.CharField(max_length=100)
    origin_Country = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
