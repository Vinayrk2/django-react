from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import User, Product
from .serializers import UserSerializer, ProductSerializer

class ProductView(APIView):
    serializer_class = ProductSerializer

    def get(self,request):
        product = [ {"name": product.name,"product": product.description,  "price": product.price} for product in Product.objects.all()]

        return Response(product) 
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return  Response(serializer.errors)


    
