from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registro, name='registro'),
    path('inicio/', views.inicio, name='inicio-sesion'),
]