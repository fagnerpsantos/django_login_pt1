from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('logar_usuario', logar_usuario, name="logar_usuario"),
    path('cadastrar_usuario', cadastrar_usuario, name="cadastrar_usuario"),
    path('index', index, name="index"),
]