from collections import deque

# Función BFS para encontrar un camino con capacidad disponible
def bfs(origen, destino, padre, capacidad, adyacencia):
    n = len(padre)
    padre[:] = [-1] * n
    padre[origen] = -2
    cola = deque([(origen, float('inf'))])

    while cola:
        actual, flujo = cola.popleft()

        for vecino in adyacencia[actual]:
            if padre[vecino] == -1 and capacidad[actual][vecino] > 0:
                padre[vecino] = actual
                nuevo_flujo = min(flujo, capacidad[actual][vecino])
                if vecino == destino:
                    return nuevo_flujo
                cola.append((vecino, nuevo_flujo))

    return 0

# Método de Ford-Fulkerson para encontrar el flujo máximo
def flujo_maximo(capacidad):

    # Validación: Comprobar que capacidad es una lista de listas (matriz)
    if not all(isinstance(row, list) for row in capacidad):
        raise ValueError("La capacidad debe ser una matriz (lista de listas).")

    # Validación: Comprobar que la matriz es cuadrada
    n = len(capacidad)
    if not all(len(row) == n for row in capacidad):
        raise ValueError("La matriz de capacidad debe ser cuadrada.")

    # Validación: Asegurarse de que los elementos de capacidad son no negativos
    for i in range(n):
        for j in range(n):
            if capacidad[i][j] < 0:
                raise ValueError("Todos los valores de capacidad deben ser no negativos.")

    origen = 0
    destino = n - 1
    padre = [-1] * n
    flujo_total = 0

    # Crear lista de adyacencia en torno a capacidad
    adyacencia = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if capacidad[i][j] > 0:
                adyacencia[i].append(j)

    # Bucle principal 
    while True:
        flujo = bfs(origen, destino, padre, capacidad, adyacencia)
        if flujo == 0:
            break
        flujo_total += flujo
        actual = destino
        while actual != origen:
            anterior = padre[actual]
            capacidad[anterior][actual] -= flujo
            capacidad[actual][anterior] += flujo
            actual = anterior

    print(f"Flujo máximo: {flujo_total}")
    return flujo_total
