from rest_framework import serializers
from .models import product,cardapio,entregas,funcionarios


class productserialazer(serializers.ModelSerializer):
    class Meta:
        model=product

        fields=['id', 'name','price']

class cardapioserialazer(serializers.ModelSerializer):
    class Meta:
        model=cardapio

        fields=['id', 'name','salario']

class entregasserialazer(serializers.ModelSerializer):
    class Meta:
        model=entregas

        fields=['id', 'local','codigo']

class funcionariosserialazer(serializers.ModelSerializer):
    class Meta:
        model=funcionarios

        fields=['id', 'name','texto']