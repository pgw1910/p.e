from django.db import models

# Create your models here.

class product(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length =50)
=======
    name = models.models.CharField(max_length =50)
>>>>>>> 2105bebb1386340779e3bf132445f6956ac0d531
    price = models.DecimalField(max_digits=5,decimal_places=2)


class funcionarios(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length =50)
=======
    name = models.models.CharField(max_length =50)
>>>>>>> 2105bebb1386340779e3bf132445f6956ac0d531
    salario = models.DecimalField(max_digits=7,decimal_places=2)


class entregas(models.Model):
<<<<<<< HEAD
    local = models.CharField(max_length =50)
=======
    local = models.models.CharField(max_length =50)
>>>>>>> 2105bebb1386340779e3bf132445f6956ac0d531
    codigo = models.IntegerField()


class cardapio(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length =50)
=======
    name = models.models.CharField(max_length =50)
>>>>>>> 2105bebb1386340779e3bf132445f6956ac0d531
    texto = models.CharField(max_length=20)
