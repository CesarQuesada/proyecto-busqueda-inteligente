import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np


def convertir_a_coordenadas(ruta, cant_filas):
    coordenadas = []
    for celda in ruta:
        if len(celda) >= 3:
            columna = int(celda[1]+celda[2]) - 1
        else:
            columna = int(celda[1]) - 1
        fila = ord('a') - ord(celda[0]) + (cant_filas - 1)
        coordenadas.append([fila, columna])
    return coordenadas


def mostrar_ruta_en_mapa(mapa, ruta):
    # Definir texturas
    texturas = {
        0: 'imagenes/zona0.png',
        1: 'imagenes/zona1.png',
        2: 'imagenes/zona2.png',
        3: 'imagenes/zona3.png',
        'ruta': 'imagenes/ruta.png'
    }

    # Convertir el archivo en una matriz
    matriz = [list(map(int, fila.strip()))for fila in mapa.strip().split('\n')]

    # Calcular el número de filas y columnas
    n, m = len(matriz), len(matriz[0])

    # Crear lista de coordenadas de la ruta
    coordenadas = convertir_a_coordenadas(ruta, n)

    # Crear una figura y ejes
    fig, ax = plt.subplots(figsize=(5.7, 5.7))
    
    # Set del zoom 
    zoomTextura = 1.7 if 8 > n >= 6 else (1.00 if n > 5 else 2.5)
    zoomRuta = 1.2 if 8 > n >= 6 else (0.75 if n > 5 else 1.55)
    
    # Dibujar la cuadrícula con las texturas y la ruta asociada
    for i in range(m):
        for j in range(n):
            textura_file = texturas[matriz[j][i]]
            img = plt.imread(textura_file)
            imagebox = OffsetImage(img, zoom=zoomTextura)
            ab = AnnotationBbox(imagebox, (i, n - 1 - j), frameon=False)
            ax.add_artist(ab)

            if [j, i] in coordenadas:
                textura_file = texturas['ruta']
                img = plt.imread(textura_file)
                imagebox = OffsetImage(img, zoom=zoomRuta)
                ab = AnnotationBbox(imagebox, (i, n - 1 - j), frameon=False)
                ax.add_artist(ab)

    # Configurar las etiquetas de las filas (letras)
    ax.set_xticks(np.arange(0, m, 1))
    ax.set_yticks(np.arange(0, n, 1))
    ax.set_xticklabels(range(1, m + 1), fontweight='bold')
    ax.set_yticklabels([chr(97 + i) for i in range(n)], fontweight='bold')

    # Configurar los límites de los ejes para mostrar completamente la cuadrícula
    ax.set_xlim(-0.5, m - 0.5)
    ax.set_ylim(-0.5, n - 0.5)

    # Ocultar las líneas de los ejes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Mostrar solo el número de casilla y las texturas
    plt.tick_params(axis='both', which='both', bottom=False, top=False,
                    labelbottom=True, left=False, right=False, labelleft=True)
    
    # Calcular el DPI necesario para mantener el tamaño y resolución especificados
    dpi = 71.575  # Establecer el DPI deseado

    # Asegurarse de que la figura se muestre con el DPI correcto
    fig.set_dpi(dpi)

    # Guardar la figura en formato .png en la carpeta "imagenes"
    fig.savefig('imagenes/solucion.png', bbox_inches='tight', pad_inches=0, dpi=dpi)


    # Cierra la figura para liberar recursos
    plt.close(fig)

    # Retornar la figura y el eje
    #return fig


if __name__=="__main__":
    
    # Mapa de prueba
    mapaNuevoTexturas ="""
            1223100032
            3232223201
            1312321201
            0023223322
            1113020012
            3303003333
            1023033232
            1200020210
            2031202021
            0230103030
            """
    
    # Ruta de Prueba
    ruta = ['b1', 'c1', 'd1', 'd2', 'd3', 'd4']
    #ruta =[]
    # Mostrar el mapa con la ruta
    mostrar_ruta_en_mapa(mapaNuevoTexturas, ruta)
    
    # Mostrar la figura
    plt.show()
