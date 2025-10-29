from django.db import models

# Create your models here.

class product(models.Model):
    name = models.models.CharField(max_length =50)
    price = models.DecimalField(max_digits=5,decimal_places=2)


class funcionarios(models.Model):
    name = models.models.CharField(max_length =50)
    salario = models.DecimalField(max_digits=7,decimal_places=2)


class entregas(models.Model):
    local = models.models.CharField(max_length =50)
    codigo = models.IntegerField()


class cardapio(models.Model):
    name = models.models.CharField(max_length =50)
    texto = models.CharField(max_length=20)
