from django.urls import path
from . import views


urlpatterns =[
    path('', views.productListGenericView, name="product-list" ),
]