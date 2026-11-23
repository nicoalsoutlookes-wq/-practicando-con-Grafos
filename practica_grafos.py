# Practica Grafos - Algoritmos de Floyd y Dijkstra
# Alumno: Rodriguez Hernandez Alberto Nicolas

INF = 999999   # representa que NO hay arista entre dos vertices


# =====================================================
# FUNCIONES AUXILIARES
# =====================================================
def imprimir_matriz(matriz, nombres):
    print("      " + "".join(f"{n:>6}" for n in nombres))
    for i in range(len(matriz)):
        fila = f"{nombres[i]:>6}"
        for j in range(len(matriz)):
            if matriz[i][j] == INF:
                fila += f"{'INF':>6}"
            else:
                fila += f"{matriz[i][j]:>6}"
        print(fila)


def obtener_camino(anterior, destino, nombres):
    camino = []
    actual = destino
    while actual != -1:
        camino.insert(0, nombres[actual])
        actual = anterior[actual]
    return " -> ".join(camino)


# =====================================================
# ALGORITMO DE FLOYD (distancias entre todos los pares)
# =====================================================
def floyd(matriz):
    n = len(matriz)
    dist = [fila[:] for fila in matriz]   # copia de la matriz

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


# =====================================================
# ALGORITMO DE DIJKSTRA (distancias desde un origen)
# =====================================================
def dijkstra(matriz, origen):
    n = len(matriz)
    dist = [INF] * n
    visitado = [False] * n
    anterior = [-1] * n
    dist[origen] = 0

    for _ in range(n):
        # buscar el vertice no visitado con menor distancia
        u = -1
        for i in range(n):
            if not visitado[i] and (u == -1 or dist[i] < dist[u]):
                u = i

        if dist[u] == INF:
            break          # los que faltan no se pueden alcanzar

        visitado[u] = True

        # revisar los vecinos de u
        for v in range(n):
            if matriz[u][v] != INF and not visitado[v]:
                if dist[u] + matriz[u][v] < dist[v]:
                    dist[v] = dist[u] + matriz[u][v]
                    anterior[v] = u
    return dist, anterior


def probar_grafo(titulo, nombres, matriz):
    print("=" * 60)
    print(titulo)
    print("=" * 60)

    print("\nMATRIZ DE ADYACENCIA:")
    imprimir_matriz(matriz, nombres)

    print("\nFLOYD - MATRIZ DE DISTANCIAS MINIMAS:")
    imprimir_matriz(floyd(matriz), nombres)

    print(f"\nDIJKSTRA - DESDE EL VERTICE {nombres[0]}:")
    dist, anterior = dijkstra(matriz, 0)
    for i in range(len(nombres)):
        if dist[i] == INF:
            print(f"  {nombres[0]} -> {nombres[i]}: no hay camino")
        else:
            print(f"  {nombres[0]} -> {nombres[i]}: distancia {dist[i]}, "
                  f"camino: {obtener_camino(anterior, i, nombres)}")
    print()


# =====================================================
# PROGRAMA PRINCIPAL (MAIN)
# =====================================================

# GRAFO 1 (vertices a, b, c, d, e - dibujo a mano)
nombres1 = ["a", "b", "c", "d", "e"]
matriz1 = [
    [0,   3,   5,   INF, INF],   # a
    [INF, 0,   2,   4,   INF],   # b
    [INF, INF, 0,   1,   7],     # c
    [INF, INF, INF, 0,   5],     # d
    [INF, INF, INF, INF, 0],     # e
]

# GRAFO 2 (vertices A, B, C, D, E)
nombres2 = ["A", "B", "C", "D", "E"]
matriz2 = [
    [0,   4,   2,   INF, INF],   # A
    [INF, 0,   2,   5,   INF],   # B
    [INF, 2,   0,   8,   10],    # C
    [INF, INF, INF, 0,   2],     # D
    [INF, INF, INF, INF, 0],     # E
]

# GRAFO 3 (vertices A, B, C, D, E)
nombres3 = ["A", "B", "C", "D", "E"]
matriz3 = [
    [0,   7,   INF, 3,   INF],   # A
    [INF, 0,   2,   INF, 6],     # B
    [INF, INF, 0,   1,   3],     # C
    [INF, 2,   INF, 0,   5],     # D
    [INF, INF, 3,   INF, 0],     # E
]

probar_grafo("GRAFO 1", nombres1, matriz1)
probar_grafo("GRAFO 2", nombres2, matriz2)
probar_grafo("GRAFO 3", nombres3, matriz3)
