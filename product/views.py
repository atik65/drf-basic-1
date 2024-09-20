from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.forms.models import model_to_dict
from .serializers import ProductSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
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

