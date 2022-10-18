from dataclasses import fields
from unicodedata import category
from rest_framework import serializers
from .models import * 

class QuantitySerializations(serializers.ModelSerializer):
    class Meta:
        model=QuantityVariant
        fields='__all__'
        

class CategorySerializations(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields='__all__'

class SizeSerializations(serializers.ModelSerializer):
    class Meta:
        model=SizeVariant
        fields='__all__'
        

class ColorSerializations(serializers.ModelSerializer):
    class Meta:
        model=ColorVariant
        fields='__all__'
        

class ProductSerializers(serializers.ModelSerializer):
    category=CategorySerializations()
    quantity_type=QuantitySerializations()
    color_type=ColorSerializations()
    size_type=SizeSerializations()
    class Meta:
        model=Product
        fields='__all__'




