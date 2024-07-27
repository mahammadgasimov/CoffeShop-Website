from django.db import models
from test.test_typechecks import Integer

# Create your models here.

class Coffe (models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2000)
    
def __str__(self):
    return self.title

    
