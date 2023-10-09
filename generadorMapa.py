import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import random

def cargar_mapa(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        mapa = archivo.read()
    return mapa

def guardar_mapa(nombre_archivo, mapa):
     with open(nombre_archivo, 'w') as archivo:
        archivo.write(mapa)

def generar_mapa_aleatorio(m, n):
    mapa = ""
    for _ in range(n):
        fila = [str(random.randint(0, 3)) for _ in range(m)]
        mapa += "".join(fila) + "\n"
    return mapa

def crear_mapa():
    mapa = """
    02121
    12212
    00120
    """
    return mapa

# Crear propio mapa
mapa = crear_mapa()

# Cargar mapa
mapa = cargar_mapa("MapaSinSolucion.txt")

# Mapa aleatorio
mapa = generar_mapa_aleatorio(10, 10)

# Guardar el mapa generado en un archivo de texto
guardar_mapa("MapaSinSolucion.txt", mapa)


#################################################
# Dibujar mapa
#################################################

# Convertir el archivo en una matriz
matriz = [[int(c) for c in fila.strip()] for fila in mapa.strip().split('\n')]

# Definir texturas
texturas = {
    0: 'imagenes/zona0.png',  # Textura 0
    1: 'imagenes/zona1.png',  # Textura 1
    2: 'imagenes/zona2.png',  # Textura 2
    3: 'imagenes/zona3.png',  # Textura 3
}

# Calcular el número de filas y columnas
m = len(matriz[0])
n = len(matriz)

# Crear una figura y ejes
fig, ax = plt.subplots()

# Dibujar la cuadrícula con las texturas
for i in range(m):
    for j in range(n):
        textura_file = texturas[matriz[j][i]]
        img = plt.imread(textura_file)
        imagebox = OffsetImage(img, zoom=1.0)
        ab = AnnotationBbox(imagebox, (i, n - 1 - j), frameon=False)
        ax.add_artist(ab)

# Configurar las etiquetas de las filas (letras)
ax.set_xticks(np.arange(0, m, 1))
ax.set_yticks(np.arange(0, n, 1))
ax.set_xticklabels(range(1, m + 1))
ax.set_yticklabels([chr(65 + i) for i in range(n)])

# Configurar los límites de los ejes para mostrar completamente la cuadrícula
ax.set_xlim(-0.5, m - 0.5)
ax.set_ylim(-0.5, n - 0.5)

# Ocultar las líneas de los ejes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Mostrar solo el numero de casilla y las texturas
plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=True, left=False, right=False, labelleft=True)

# Mostrar el mapa
plt.show()
