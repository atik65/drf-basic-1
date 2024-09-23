from django.shortcuts import render
from product import models
from product import serializers

from rest_framework import generics


# generic product list view
class ProductListGeneric(generics.ListAPIView):
    queryset = models.Product.objects.all();
    serializer_class = serializers.ProductSerializer

productListGenericView = ProductListGeneric.as_view()