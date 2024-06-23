import random
from rest_framework.response import Response
from rest_framework import viewsets, status, views

from .models import Product, User
from .serializers import ProductSerializer
from .producer import publish


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        print('qkwe;rjqw;e+++++++++++++++++++++++++++++++++')

        publish('product_created', serializer.data)


        return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

    def update(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        publish('product_updated', serializer.data)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, pk=None):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()

            # publish('product_destroyed', product.pk)
            publish('product_deleted', {'id': pk})

            return Response(
                {
                    'message': 'Product deleted successfully'
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except Product.DoesNotExist:
            publish('product_not_found', {'id':pk})
            return Response(
                {
                    'error': 'Product not found'
                },
                status=status.HTTP_404_NOT_FOUND
            )


class UserAPIView(views.APIView):
    def get(self, request):
        users = User.objects.all()
        user = random.choice(users)
        return Response(
            {
                'user': user.id
            }
        )




