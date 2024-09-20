from django.shortcuts import render
from django.http import JsonResponse

def homeView(request):
    
    print('params : ', request.GET)

    return JsonResponse({"message": "Hey hello"})


def contactView ( request ):

    res_dict = {
        "message": "Contact View"
    }

    return JsonResponse(res_dict)