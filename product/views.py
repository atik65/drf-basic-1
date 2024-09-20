from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.forms.models import model_to_dict


# Create your views here.
def productView(request, *args, **kwargs):

    try:
        products = models.Product.objects.all().first()
    except Exception as e:
        print('error = ', e)

    # response back product dict to json with default model_to_dict method

    return JsonResponse({"products": model_to_dict(products)})