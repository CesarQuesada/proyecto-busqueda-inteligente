'''
Los métodos "buscar_solucion_UCS()" y "buscar_solucion_BFS()" fueron tomados del libro:
INTELIGENCIA ARTIFICIAL, Fundamentos, práctica y aplicaciones.
Alberto García Serrano, 2012, pag 43 y pag 61. 
'''
from arbol import Nodo
from mapas import *
import threading

class Metodo_de_Busqueda(Nodo):
    def __init__(self, mapaElegido, estado_inicial,solucion):
        self.mapaElegido = mapaElegido
        self.estado_inicial = estado_inicial
        self.solucion = solucion

        self.nodos_comunes = []
        self.solucionado = False
        self.soluciones_bidir = [None, None]
        self.turn = 0

    # Código para el algoritmo de búsqueda por coste uniforme:
    def buscar_solucion_UCS(self, estado_inicial=None, num_hilo=None):
        if estado_inicial == None:
            estado_inicial = self.estado_inicial

        nodo_inicial = Nodo(estado_inicial)
        nodo_inicial.set_coste(0)   
        nodos_frontera = [nodo_inicial]
        nodos_visitados = []

        # Los métodos "compara" y "comp_to_key" lo único que hacen es indicarle al método "sorted" cómo ordenar los elementos.
        def compara(x,y):
            return x.get_coste() - y.get_coste()
        def cmp_to_key(mycmp):
            'Convert a cmp= function into a key= function'
            class K:
                def __init__(self, obj, *args):
                    self.obj = obj
                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0
                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0
                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0
                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0
                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0
                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0
            return K

        while not self.solucionado and len(nodos_frontera) != 0:
            if num_hilo != None:
                while self.turn != num_hilo:
                    pass  # Espera hasta que sea el turno del hilo actual
                self.turn = 1 - num_hilo  # Cambia el turno al otro hilo

            #Se ordena la lista de nodos frontera:
            nodos_frontera = sorted(nodos_frontera, key = cmp_to_key(compara))
            nodo=nodos_frontera[0]

            #Se extrae el nodo y se añade a los nodos visitados:
            nodos_visitados.append(nodos_frontera.pop(0))
            self.nodos_comunes.append(nodos_visitados[-1])

            # Para búsqueda bidireccional, buscar si el nodo ya está en la lista de nodos comunes
            if (num_hilo != None and nodo.en_lista(self.nodos_comunes[:-1])):
                if not self.solucionado:
                    self.soluciones_bidir[num_hilo] = nodo
                    self.solucionado = True
                    return

            elif (nodo.get_datos() == self.solucion and num_hilo == None):
                #Solucion encontrada
                self.solucionado = True
                return nodo
            
            else:
                #Se expanden los nodos hijos (casillas siguientes que se pueden recorrer)
                dato_nodo = nodo.get_datos()
                lista_hijos = []
                for un_hijo in self.mapaElegido[dato_nodo]:
                    hijo = Nodo(un_hijo)
                    coste = self.mapaElegido[dato_nodo][un_hijo]
                    hijo.set_coste(nodo.get_coste() + coste)
                    lista_hijos.append(hijo)

                    if not hijo.en_lista(nodos_visitados):
                        if hijo.en_lista(nodos_frontera):
                            for n in nodos_frontera:
                                if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                                    nodos_frontera.remove(n)
                                    nodos_frontera.append(hijo)
                        else:
                            nodos_frontera.append(hijo)
                nodo.set_hijos(lista_hijos)

        # Obtener la solución para el hilo donde ya se habia visto la solucion
        if num_hilo != None and num_hilo != self.turn:
            for nodo in nodos_visitados:
                if nodo.get_datos() == self.soluciones_bidir[num_hilo ^ 0b1].get_datos():
                    self.soluciones_bidir[self.turn ^ 0b1] = nodo.get_padre()
            
            
    # Código para el algoritmo de búsqueda por amplitud:
    def buscar_solucion_BFS(self, estado_inicial=None, num_hilo=None):
        if num_hilo == None:
            estado_inicial = self.estado_inicial

        nodo_inicial = Nodo(estado_inicial)
        nodos_frontera = [nodo_inicial]
        nodos_visitados = []

        while not self.solucionado and len(nodos_frontera) != 0:
            if num_hilo != None:
                while self.turn != num_hilo:
                    pass # Espera hasta que sea el turno del hilo actual
                self.turn = 1 - num_hilo  # Cambia el turno al otro hilo

            nodo = nodos_frontera[0]

            #Se extrae el nodo y se añade a visitados
            nodos_visitados.append(nodos_frontera.pop(0))
            self.nodos_comunes.append(nodos_visitados[-1])

            # Para búsqueda bidireccional, buscar si el nodo ya está en la lista de nodos comunes
            if (num_hilo != None and nodo.en_lista(self.nodos_comunes[:-1])):
                self.soluciones_bidir[num_hilo] = nodo
                self.solucionado = True
                return

            elif (num_hilo == None and nodo.get_datos() == self.solucion):
                #Solucion encontrado
                self.solucionado = True
                return nodo
            
            else: 
                #expandir nodos hijo (casillas siguientes que se pueden recorrer)
                dato_nodo = nodo.get_datos()
                lista_hijos = []
                for un_hijo in self.mapaElegido[dato_nodo]:
                    hijo = Nodo(un_hijo)
                    lista_hijos.append(hijo)
                    if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                        nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

        # Obtener la solución para el hilo donde donde ya se habia visto la solucion
        if num_hilo != None and num_hilo != self.turn:
            for nodo in nodos_visitados:
                if nodo.get_datos() == self.soluciones_bidir[num_hilo ^ 0b1].get_datos():
                    self.soluciones_bidir[self.turn ^ 0b1] = nodo
                    

    # Código para el algoritmo de búsqueda bidireccional
    def buscar_solucion_Bidireccional(self, algoritmo:str):
        desde_inicio = None
        desde_fin = None

        if algoritmo.lower() == "ucs":
            # Crear hilos
            desde_inicio = threading.Thread(target=self.buscar_solucion_UCS, args=(self.estado_inicial, 0,))
            desde_fin = threading.Thread(target=self.buscar_solucion_UCS, args=(self.solucion, 1,))

        elif algoritmo.lower() == "bfs":
            # Crear hilos
            desde_inicio = threading.Thread(target=self.buscar_solucion_BFS, args=(self.estado_inicial, 0))
            desde_fin = threading.Thread(target=self.buscar_solucion_BFS, args=(self.solucion, 1,))

        else: return None
        
        # Iniciar los hilos
        desde_inicio.start()
        desde_fin.start()

        # Esperar a que ambos hilos terminen
        desde_inicio.join()
        desde_fin.join()

        # Coste parcial
        try: coste = self.soluciones_bidir[0].get_coste() + self.soluciones_bidir[1].get_coste()
        except: coste = None

        # Reconstruccion del camino
        existentes = []
        nodo_actual = self.soluciones_bidir[0]
        
        while (nodo_actual.get_padre() != None):
            existentes.append(nodo_actual.get_datos())
            nodo_actual = nodo_actual.get_padre()

        while (self.soluciones_bidir[1] != None):
            if not self.soluciones_bidir[1].get_datos() in existentes:
                hijos = []
                hijos.append(Nodo(self.soluciones_bidir[1].get_datos()))
                self.soluciones_bidir[0].set_hijos(hijos)
                self.soluciones_bidir[0] = self.soluciones_bidir[0].get_hijos().pop(0)
                
            self.soluciones_bidir[1] = self.soluciones_bidir[1].get_padre()

        # Coste final (sumando el movimiento final)
        if coste != None: self.soluciones_bidir[0].set_coste(coste + self.mapaElegido[self.soluciones_bidir[0].get_padre().get_datos()][self.soluciones_bidir[0].get_datos()])

        return self.soluciones_bidir[0]

###########################################################################################################################################################################
# Esta sección del código está para cuando se quiera ejecutar sólo el archivo "ambasBusquedas.py" sin necesidad de ejecutar la interfaz.
# Es posible probar los algoritmos desde una terminal.

if __name__=="__main__":
    mapaEscogido = Mapa.mapa3
    origen = input("Ingrese origen: " )
    destino = input("Ingrese destino: ")

    tipoDeCalculo = input("Digite:\n1) Calcular la ruta con menos consumo de energía \n2) Calcular la ruta más corta\n3) Calcular la ruta con menos consumo de energía (algoritmo bidireccional)\n4) Calcular la ruta más corta (algoritmo bidireccional)\n")
    if tipoDeCalculo == '1':
        nodo_solucion = Metodo_de_Busqueda(mapaEscogido, origen, destino).buscar_solucion_UCS()
        
    elif tipoDeCalculo == '2':
        nodo_solucion = Metodo_de_Busqueda(mapaEscogido, origen, destino).buscar_solucion_BFS()
        
    elif tipoDeCalculo == '3':
        nodo_solucion = Metodo_de_Busqueda(mapaEscogido, origen, destino).buscar_solucion_Bidireccional('UCS')

    elif tipoDeCalculo == '4':
        nodo_solucion = Metodo_de_Busqueda(mapaEscogido, origen, destino).buscar_solucion_Bidireccional('BFS')

    else:
        print("No digito una opción válida, intente nuevamente.") 

    #Mostrar resultado:
    resultado = []
    nodo = nodo_solucion 

    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre() 
        
    resultado.append(origen) 
    resultado.reverse()
    print(f"\nResultado: {resultado}")
    print("Coste: " + str(nodo_solucion.get_coste()))
#############################################################################################################################################################################