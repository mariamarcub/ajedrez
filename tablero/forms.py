from django import forms

class CreaTableroForm(forms.Form): #forms es la librería y form es la clase
    tamano_casilla = forms.IntegerField(min_value=20, max_value=100, label='Tamaño de las casillas', initial=20)





