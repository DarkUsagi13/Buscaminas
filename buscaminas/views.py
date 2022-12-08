from django.shortcuts import render
from .forms import FormTablero
from .minas_obj import Tablero


# Create your views here.


def welcome(request):
    return render(request, 'buscaminas/welcome.html', {})


def crear_tablero(request):
    form = FormTablero(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            filas = form.cleaned_data['filas']
            columnas = form.cleaned_data['columnas']
            minas = form.cleaned_data['minas']
            tablero = Tablero(filas, columnas, minas)
            coordenadas = tablero.coordenadas()
            return render(request, 'buscaminas/muestra_tablero.html', {'tablero': tablero, 'coordenadas': coordenadas})
        else:
            form = FormTablero()
    return render(request, 'buscaminas/crear_tablero.html', {'form': form})
