from rest_framework import viewsets
from .models import NetworkNode, Product
from .serializers import NetworkNodeSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticated


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['country']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
