from django.urls import path
from .views import ProductListCreateAPIView
from . import views

urlpatterns = [
    path('produtos/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('', views.home, name='home'),
]
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls
