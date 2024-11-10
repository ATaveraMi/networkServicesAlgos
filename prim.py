
import heapq
from typing import Tuple, List
def leer_grafo_ponderado(ruta_archivo : str)->List[List[int]]:
    """Lee una matriz de adyacencia desde un archivo y la convierte en una lista de listas."""
    with open(ruta_archivo, 'r') as archivo:
        matriz: List[List[int]] = []
        for linea in archivo:
            fila: List[int] = [int(valor) if valor != '-1' else float('inf') for valor in linea.strip().split()]
            matriz.append(fila)
        
    return matriz

def prim_mst(matriz):
    """Implementa el algoritmo de Prim para encontrar el MST en un grafo ponderado."""
    num_nodos:int = len(matriz)
    visitados: List[int] = [False] * num_nodos  # Para rastrear nodos visitados
    mst_edges:List[Tuple[int,int,int]] = []  # Lista para almacenar las aristas del MST
    min_heap = [(0, 0, -1)]  # (peso, nodo actual, nodo previo)
    total_peso:int = 0  # Peso total del MST

    while min_heap:
        peso, nodo, previo = heapq.heappop(min_heap)

        if visitados[nodo]:
            continue

        visitados[nodo] = True
        total_peso += peso

        # Si no es el nodo inicial, agregamos la arista al MST
        if previo != -1:
            mst_edges.append((previo, nodo, peso))

        # Agregamos las aristas adyacentes al heap
        for vecino in range(num_nodos):
            if not visitados[vecino] and matriz[nodo][vecino] != float('inf'):
                heapq.heappush(min_heap, (matriz[nodo][vecino], vecino, nodo))
    #print(mst_edges)
        

    return mst_edges, total_peso

# Leer la matriz de adyacencia
ruta_archivo: str = 'grafo.txt'
matriz_adyacencia: List[List[int]] = leer_grafo_ponderado(ruta_archivo)

# Encontrar el MST (Minimum Spanning Tree)
mst_edges, total_peso = prim_mst(matriz_adyacencia)


print("Conexiones óptimas para el cableado entre colonias:")
for u, v, peso in mst_edges:
    print(f"Colonia {u+1} - Colonia {v+1} : {peso} km")

print(f"Longitud total mínima de cableado: {total_peso} km")

