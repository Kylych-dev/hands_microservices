import random

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status, views

from .models import Product, User
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

    def retrieve(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        product.delete()


class UserAPIView(views.APIView):
    def get(self, request):
        users = User.objects.all()
        user = random.choice(users)
        return Response(
            {
                'user': user.id
            }
        )




