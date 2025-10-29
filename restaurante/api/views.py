from rest_framework import viewsets
from .models import product,cardapio,entregas,funcionarios
from .serializers import productroductserialazer,cardapioserialazer,entregasserialazer,funcionariosserialazer

# Create your views here.
class productViewset(viewsets.ModelViewSet):
 queryset = product.objects.all()
 serializer_class = productroductserialazer

class cardapioViewSet(viewsets.ModelViewSet):
 queryset = cardapio.objects.all()
 serializer_class =cardapioserialazer
 
class entregasViewSet(viewsets.ModelViewSet):
 queryset = entregas.objects.all()
 serializer_class =entregasserialazer
 
class funcionariosViewSet(viewsets.ModelViewSet):
 queryset = funcionarios.objects.all()
 serializer_class =funcionariosserialazer