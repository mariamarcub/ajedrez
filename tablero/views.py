from django.shortcuts import render
from .forms import CreaTableroForm
from .ajedrez import crear_tablero

def index(request):
    return render(request, 'tablero/index.html', {})


def crea_tablero(request):
    tamano_casilla = None
    form = CreaTableroForm()  # Asegúrate de inicializar el formulario aquí
    if request.method == 'POST':
        form = CreaTableroForm(request.POST)
        if form.is_valid():
            tamano_casilla = form.cleaned_data['tamano_casilla']
            # Genera el tablero de ajedrez con colores
            tablero = crear_tablero(tamano_casilla)
            return render(request, 'tablero/muestra_tablero.html', {'tablero': tablero, 'tamano_casilla': tamano_casilla})

    # Si llegas aquí, significa que estás renderizando la plantilla 'crea_tablero.html'
    return render(request, 'tablero/crea_tablero.html', {'form': form})


