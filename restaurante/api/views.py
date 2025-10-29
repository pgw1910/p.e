from rest_framework import viewsets, generics
from .models import product,cardapio,entregas,funcionarios
from .serializers import productserialazer, cardapioserialazer, entregasserialazer, funcionariosserialazer
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'api/index.html')

class ProductViewSet(viewsets.ModelViewSet):
 queryset = product.objects.all()
 serializer_class = productserialazer

class cardapioViewSet(viewsets.ModelViewSet):
 queryset = cardapio.objects.all()
 serializer_class =cardapioserialazer
 
class entregasViewSet(viewsets.ModelViewSet):
 queryset = entregas.objects.all()
 serializer_class =entregasserialazer
 
class funcionariosViewSet(viewsets.ModelViewSet):
 queryset = funcionarios.objects.all()
 serializer_class =funcionariosserialazer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = productserialazer