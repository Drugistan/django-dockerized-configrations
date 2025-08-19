from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.FloatField(source='get_discounted_price', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'