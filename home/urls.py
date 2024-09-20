from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="home" ),
    path('contact', views.contactView, name="contact" ),
]