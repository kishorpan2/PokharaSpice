from rest_framework.response import Response
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProductView(APIView):
    def get(self,request):
        queryset=Product.objects.all()
        serializer = ProductSerializers(queryset, many=True)
        return Response(serializer.data)

class DemoView(APIView):
    permission_classes = [IsAuthenticated] 
    def get(self, request):
        return Response({'success':"You are authenticated"})

class ProductView(APIView):
    def get(self,request):
        category= self.request.query_params.get('category_name')
        if category:
            queryset=Product.objects.filter(category__category_name= category)
        else:
            queryset=Product.objects.all()
        serializers = ProductSerializers(queryset, many= True)
        return Response({'count':len(serializers.data), 'data':serializers.data})