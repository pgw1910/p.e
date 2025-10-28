from rest_framework import serializers
from .models import product  

class productserialazer(serializers.ModelSerializer):
    class meta:
        model=product

        fields=['id', 'name','price']