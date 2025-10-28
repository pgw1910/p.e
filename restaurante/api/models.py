from django.db import models

# Create your models here.

class product (models.Model):
    name = models.models.CharField(max_length =50)
    price = models.DecimalField(max_digits=5,decimal_places=2)


    def __str__ (self):
        return self.name
