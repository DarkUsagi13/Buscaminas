from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('crear_tablero', views.crear_tablero, name='crear_tablero'),
    path('muestra_tablero', views.crear_tablero, name='muestra')
]