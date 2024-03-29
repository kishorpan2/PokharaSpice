from rest_framework import serializers
from .models import * 
from products.serializers import *

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart
        fields = '__all__'

class CartItemsSerializer(serializers.ModelSerializer):
    product= ProductSerializers()
    cart= CartSerializer
    class Meta:
        model= CartItem
        fields= '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Orders
        fields ='__all__'