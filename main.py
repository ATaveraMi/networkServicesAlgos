import pytest
from ford import flujo_maximo
from tsp import tsp

def test_tsp_resultado_correcto():
    distancias = [
        [0, 48, 12, 18],
        [52, 0, 42, 32],
        [18, 46, 0, 56],
        [24, 36, 52, 0]
    ]
    nodo_inicial = 0
    ruta_optima = tsp(distancias, nodo_inicial)
    
    assert ruta_optima is not None
    assert len(ruta_optima) == len(distancias)

def test_tsp_matriz_vacia():
    distancias = []
    nodo_inicial = 0
    with pytest.raises(ValueError, match="La matriz de distancias no puede estar vacía."):
        tsp(distancias, nodo_inicial)

def test_tsp_matriz_no_cuadrada():
    distancias = [
        [0, 48, 12],
        [52, 0, 42],
        [18, 46]
    ]
    nodo_inicial = 0
    with pytest.raises(ValueError, match="La matriz de distancias debe ser cuadrada"):
        tsp(distancias, nodo_inicial)

def test_tsp_valores_negativos():
    distancias = [
        [0, 48, -12, 18],
        [52, 0, 42, 32],
        [18, 46, 0, 56],
        [24, 36, 52, 0]
    ]
    nodo_inicial = 0
    with pytest.raises(ValueError, match="El valor en la posición"):
        tsp(distancias, nodo_inicial)

def test_tsp_ruta_conocida():
    distancias = [[0, 48, 12, 18],
                  [52, 0, 42, 32],
                  [18, 46, 0, 56],
                  [24, 36, 52, 0]]
    nodo_inicial = 0

    ruta = tsp(distancias, nodo_inicial)
    assert ruta == [(0, 2), (2, 1), (1, 3), (3, 0)]

def test_tsp_ruta_conocida():
    distancias = [[0, 48, 12, 18],
                  [52, 0, 42, 32],
                  [18, 46, 0, 56],
                  [24, 36, 52, 0]]
    nodo_inicial = 0

    ruta = tsp(distancias, nodo_inicial)
    assert ruta == [(0, 2), (2, 1), (1, 3), (3, 0)]  

def test_tsp_ruta_conocida_grande():
    distancias =[
    [0, 54, 49, 94, 63, 16, 86, 66, 71, 90],
    [61, 0, 13, 16, 33, 56, 95, 60, 89, 7],
    [57, 28, 0, 94, 42, 87, 97, 22, 62, 97],
    [83, 32, 90, 0, 65, 34, 61, 6, 24, 4],
    [63, 95, 16, 50, 0, 47, 90, 52, 66, 49],
    [93, 86, 84, 51, 76, 0, 9, 17, 46, 23],
    [90, 10, 88, 35, 96, 62, 0, 50, 86, 93],
    [49, 85, 6, 39, 30, 19, 58, 0, 62, 56],
    [44, 58, 79, 61, 4, 48, 44, 93, 0, 48],
    [50, 79, 85, 16, 15, 35, 99, 94, 100, 0]
    ]
    
    nodo_inicial = 0

    ruta = tsp(distancias, nodo_inicial)
    assert ruta == [(0, 5), (5, 6), (6, 1), (1, 9), (9, 3), (3, 8), (8, 4), (4, 2), (2, 7), (7, 0)]


# Caso de prueba 1: Gráfico simple con flujo máximo conocido
def test_flujo_maximo_simple():
    capacidad = [
        [0, 10, 10, 0, 0, 0],
        [0, 0, 5, 15, 0, 0],
        [0, 0, 0, 10, 10, 0],
        [0, 0, 0, 0, 10, 10],
        [0, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 0]
    ]
    assert flujo_maximo(capacidad) == 20

# Caso de prueba 1: Gráfico simple con flujo máximo conocido, esta en canvas
def test_flujo_maximo_simple_dos():
    capacidad = [
        [0, 48, 12, 18],
        [52, 0, 42, 32],
        [18, 46, 0, 56],
        [24, 36, 52, 0]
    ]

    assert flujo_maximo(capacidad) == 78

# Caso de prueba 2: Gráfico sin flujo posible
def test_flujo_maximo_sin_flujo():
    capacidad = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert flujo_maximo(capacidad) == 0

# Caso de prueba 3: Gráfico con solo un camino directo
def test_flujo_maximo_un_camino():
    capacidad = [
        [0, 5, 0],
        [0, 0, 5],
        [0, 0, 0]
    ]
    assert flujo_maximo(capacidad) == 5

# Caso de prueba 4: Gráfico más complejo con múltiples caminos y capacidad diversa
def test_flujo_maximo_multiples_caminos():
    capacidad = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    assert flujo_maximo(capacidad) == 23

# Caso de prueba 5: Validación - capacidad no es una lista de listas
def test_flujo_maximo_invalid_format():
    with pytest.raises(ValueError, match="La capacidad debe ser una matriz"):
        flujo_maximo([0, 1, 2])

# Caso de prueba 6: Validación - matriz no cuadrada
def test_flujo_maximo_non_square_matrix():
    capacidad = [
        [0, 10, 10],
        [0, 0, 5]
    ]
    with pytest.raises(ValueError, match="La matriz de capacidad debe ser cuadrada"):
        flujo_maximo(capacidad)

# Caso de prueba 7: Validación - capacidad negativa
def test_flujo_maximo_negative_capacity():
    capacidad = [
        [0, -10, 10],
        [0, 0, 5],
        [0, 0, 0]
    ]
    with pytest.raises(ValueError, match="Todos los valores de capacidad deben ser no negativos"):
        flujo_maximo(capacidad)
