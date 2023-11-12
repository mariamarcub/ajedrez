from django.shortcuts import render
from .forms import CreaTableroForm

def index(request):
    return render(request, 'tablero/index.html', {})

def crea_tablero(request):
    if request.method == 'POST':
        tableroform = CreaTableroForm(request.POST)
        if tableroform.is_valid():
            tamano_casilla = tableroform.cleaned_data['tamano_casilla']

            # Calcular el rango de filas y columnas
            filas = 8
            columnas = 8
            filas_range = range(filas)
            columnas_range = range(columnas)

            return render(request, 'tablero/muestra_tablero.html', {'tamano_casilla': tamano_casilla, 'filas_range': filas_range, 'columnas_range': columnas_range})
    else:
        tableroform = CreaTableroForm()

    return render(request, 'tablero/crea_tablero.html', {'form': tableroform})


