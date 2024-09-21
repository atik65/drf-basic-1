from django.urls import path
from . import views


urlpatterns = [
    path('', views.productView, name="product" ),
    path('drf/', views.productViewDrf, name="product-drf" ),
    path('create/', views.createProduct, name="create-product" ),
]