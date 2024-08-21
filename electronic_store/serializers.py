from rest_framework import serializers
from .models import NetworkNode, Product


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = '__all__'
        read_only_fields = ('debt', 'created_at')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
