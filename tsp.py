from itertools import permutations

def tsp(distancias, inicio):

    num_filas = len(distancias)
    
    # Verificar si la matriz no está vacía
    if num_filas == 0:
        raise ValueError("La matriz de distancias no puede estar vacía.")

    # Verificar si la matriz es cuadrada
    for fila in distancias:
        if len(fila) != num_filas:
            raise ValueError("La matriz de distancias debe ser cuadrada (n x n).")

    # Verificar si contiene valores no negativos
    for i in range(num_filas):
        for j in range(num_filas):
            if distancias[i][j] < 0:
                raise ValueError(f"El valor en la posición ({i}, {j}) es negativo: {distancias[i][j]}.")

    num_nodos = len(distancias)
    
    # Crear lista de nodos excepto el nodo inicial
    otros_nodos = [i for i in range(num_nodos) if i != inicio]

    # Almacenar la mejor ruta y el menor costo
    mejor_ruta = None
    menor_costo = float('inf')

    # Generar todas las permutaciones de los nodos restantes
    for permutacion in permutations(otros_nodos):
        costo_actual = 0
        nodo_actual = inicio

        # Calcular el costo de la ruta actual
        for siguiente_nodo in permutacion:
            costo_actual += distancias[nodo_actual][siguiente_nodo]
            nodo_actual = siguiente_nodo

        # Agregar el costo de regresar al nodo inicial
        costo_actual += distancias[nodo_actual][inicio]

        # Actualizar la mejor ruta si el costo es menor
        if costo_actual < menor_costo:
            menor_costo = costo_actual
            mejor_ruta = (inicio,) + permutacion

    # Generar la lista de conexiones como tuplas
    ruta_optima = [(mejor_ruta[i], mejor_ruta[i+1]) for i in range(len(mejor_ruta)-1)]
    ruta_optima.append((mejor_ruta[-1], mejor_ruta[0]))  # Añadir la conexión de regreso al inicio

    return ruta_optima


# # Código Principal
# if __name__ == "__main__":
#     # Matriz de distancias
#     distancias = [[0, 48, 12, 18],
#                 [52, 0, 42, 32],
#                 [18, 46, 0, 56],
#                 [24, 36, 52, 0]]
    
#     nodo_inicial = 0  # Nodo de inicio
    
#     ruta = tsp(distancias, nodo_inicial)
#     print("Ruta óptima:", ruta)

