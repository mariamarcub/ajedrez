def determinar_color(fila, columna):

    #Función para determinar el color de una casilla en el tablero de ajedrez.
    if (fila + columna) % 2 == 0:
        return 'amarillo'
    else:
        return 'negro'

def crear_tablero(tamano_casilla):

    # Función para crear un tablero de ajedrez.
    tablero = [] # lista vacía que servirá como el contenedor principal para representar el tablero de ajedrez.

    #Imágenes
    piezas_blancas = ['torreblanca.jpg', 'caballoblanco.jpg', 'alfilblanco.jpg', 'reinablanca.png', 'reyblanco.jpg', 'alfilblanco.jpg', 'caballoblanco.jpg', 'torreblanca.jpg']

    piezas_negras = ['torrenegra.png', 'caballonegro.jpg', 'alfilnegra.jpg', 'reinanegra.png','reynegro.jpg', 'alfilnegra.jpg', 'caballonegro.jpg', 'torrenegra.png']

    for fila in range(8): #recorremos las 8 filas
        fila_tablero = [] #almaceno las filas del tablero
        for columna in range(8):
            color = determinar_color(fila, columna) #llamamos a la funcion determinar_color

            # Añadir imágenes en la primera y última fila
            if fila == 0:
                pieza = piezas_blancas[columna]
                fila_tablero.append({'valor': pieza, 'color': color, 'tamano_casilla': tamano_casilla})
            elif fila == 7:
                pieza = piezas_negras[columna]
                fila_tablero.append({'valor': pieza, 'color': color, 'tamano_casilla': tamano_casilla})

            # Añadir imágenes de peones en la segundas y penúltima fila
            elif fila == 1:
                pieza = ['peonblanco.png']
                fila_tablero.append({'valor': pieza, 'color': color, 'tamano_casilla': tamano_casilla})

            elif fila == 6:
                pieza = ['peonnegro.png']
                fila_tablero.append({'valor': pieza, 'color': color, 'tamano_casilla': tamano_casilla})
            else:
                fila_tablero.append({'valor': '', 'color': color, 'tamano_casilla': tamano_casilla})

            #en VALOR es donde íria la figura que va en la casilla o nada si no queremos que haya nada

        tablero.append(fila_tablero)#Introducimos toda la información acumulada sobre el tablero

    return tablero #Matriz que representa el tablero con información sobre cada casilla.