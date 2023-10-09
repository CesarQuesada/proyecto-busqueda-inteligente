def generar_diccionario_vecinos(mapa):
    # Convertir el mapa en una lista de listas de enteros
    filas = mapa.strip().split('\n')
    matriz = [[int(c) for c in fila] for fila in filas]

    # Obtener las dimensiones del mapa
    m = len(matriz[0])
    n = len(matriz)

    # Definir las posiciones de los vecinos
    posiciones_vecinos = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    # Función para verificar si una casilla está dentro del mapa y no es 0
    def es_valida(x, y):
        return 0 <= x < m and 0 <= y < n and matriz[y][x] != 0

    # Generar el diccionario de vecinos para cada casilla no nula
    diccionario_vecinos = {}
    for y in range(n):
        for x in range(m):
            valor = matriz[y][x]
            if valor != 0:
                vecinos = {}
                for dx, dy in posiciones_vecinos:
                    nx, ny = x + dx, y + dy
                    if es_valida(nx, ny):
                        vecinos[f'{chr(ord("a") + n - 1 - ny )}{nx + 1}'] = matriz[ny][nx]
                diccionario_vecinos[f'{chr(ord("a") + n - 1 - y )}{x + 1}'] = vecinos

    return diccionario_vecinos

#Abrir el mapa generado por generadorMapa.py
with open("MapaSinSolucion.txt", 'r') as archivo:
        mapa = archivo.read()

diccionario_vecinos = generar_diccionario_vecinos(mapa)
for casilla, vecinos in diccionario_vecinos.items():
    print(f'{casilla}: {vecinos}')