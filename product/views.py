from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.forms.models import model_to_dict
from .serializers import ProductSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics



# product view without drf -- core django rest api
def productView(request, *args, **kwargs):

    try:
        products = models.Product.objects.all().first()
    except Exception as e:
        print('error = ', e)

    # response back product dict to json with default model_to_dict method

    return JsonResponse({"products": model_to_dict(products)})


# product api view with django rest framework

@api_view(['GET'])
def productViewDrf(request, *args, **kwargs):

    instance = models.Product.objects.all()

    data ={}

    if instance:
        data = ProductSerializer(instance, many=True).data


    return Response(data)



# create product
@api_view(["POST"])
def createProduct(request, *args, **kwargs):

    serializer = ProductSerializer(data= request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


    return Response({
        'message': 'Something went wrong'
    },status=500)


class ProductDetailsGeneric(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


productDetailsGenericView = ProductDetailsGeneric.as_view()
    