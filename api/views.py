from django.shortcuts import get_list_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from product.models import Product

from .serializers import ProductSerializer


# ----------------------------API Endpoints---------------------------- #


# ----------------------------Products---------------------------- #


@api_view(['GET'])
def get_all_products(request):
    """
    app: product
    resource: Product
    methods: GET
    response: a list of all products from db
    """

    products = Product.objects.all().order_by('title')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
