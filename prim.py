def prim(matriz_adyacencia):
    """Encuentra el árbol de expansión mínima (MST) usando el algoritmo de Prim."""
    num_nodos = len(matriz_adyacencia)
    INFINITO = float('inf')
    peso_total = 0
    visitado = [False] * num_nodos  # Nodos ya seleccionados para el MST
    aristas_minimas = [{'peso': INFINITO, 'origen': -1} for _ in range(num_nodos)]
    aristas_minimas[0]['peso'] = 0  # Comenzar desde el nodo 0

    mst = []  # Almacena las aristas del MST

    for _ in range(num_nodos):
        nodo_actual = -1
        for nodo in range(num_nodos):
            if not visitado[nodo] and (nodo_actual == -1 or aristas_minimas[nodo]['peso'] < aristas_minimas[nodo_actual]['peso']):
                nodo_actual = nodo

        if aristas_minimas[nodo_actual]['peso'] == INFINITO:
            raise ValueError("¡No es posible construir un MST! El grafo no es conexo.")

        visitado[nodo_actual] = True
        peso_total += aristas_minimas[nodo_actual]['peso']

        if aristas_minimas[nodo_actual]['origen'] != -1:
            mst.append((aristas_minimas[nodo_actual]['origen'], nodo_actual))

        for nodo_destino in range(num_nodos):
            if matriz_adyacencia[nodo_actual][nodo_destino] != -1 and matriz_adyacencia[nodo_actual][nodo_destino] < aristas_minimas[nodo_destino]['peso']:
                aristas_minimas[nodo_destino] = {'peso': matriz_adyacencia[nodo_actual][nodo_destino], 'origen': nodo_actual}

    return mst, peso_total


# Matriz de adyacencia proporcionada directamente en el código
grafo = [
    [0, 2, -1, 6, -1],
    [2, 0, 3, 8, 5],
    [-1, 3, 0, -1, 7],
    [6, 8, -1, 0, 9],
    [-1, 5, 7, 9, 0]
]

# Código principal
if __name__ == "__main__":
    try:
        arbol_expansion_minima, peso_total = prim(grafo)
        
        # Imprimir las aristas en el formato deseado
        print("Aristas del MST (forma óptima de cablear):")
        print(", ".join(f"({origen}, {destino})" for origen, destino in arbol_expansion_minima))
    except Exception as error:
        print(f"Error: {error}")
