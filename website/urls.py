from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('comida/', views.comida, name='comida'),
    path('bebidas/', views.bebidas, name='bebidas'),
    path('snacks/', views.snacks, name='snacks'),
    path('actividadesDesportivas/', views.actividadesDesportivas, name='actividadesDesportivas'),
]
