import copy
#EXAMEN T3 ANALISIS DE ALGORITMOS Y ESTRATEGIAS DE PROGRAMACION 
#ALUMNO: JHERSON ALBERTO HUANUCO TRUJILLO

def resolver_laberinto(laberinto, fila, columna, camino, puntos_actuales, visitado, fila_fin, columna_fin, puntos_minimos_requeridos):
    
    filas = len(laberinto)
    columnas = len(laberinto[0])

    if not (0 <= fila < filas and 0 <= columna < columnas):
        return False
    if laberinto[fila][columna] == 0:
        return False
    if (fila, columna) in visitado:
        return False

    camino.append((fila, columna))
    visitado.add((fila, columna))

    valor_celda = laberinto[fila][columna]
    if valor_celda in [3, 4]:
        puntos_actuales += valor_celda

    if fila == fila_fin and columna == columna_fin:
        if puntos_actuales >= puntos_minimos_requeridos:
            return True
        else:
            camino.pop()
            visitado.remove((fila, columna))
            return False

    direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)] 

    for df, dc in direcciones:
        siguiente_fila, siguiente_columna = fila + df, columna + dc
        if resolver_laberinto(laberinto, siguiente_fila, siguiente_columna, camino, puntos_actuales, visitado, fila_fin, columna_fin, puntos_minimos_requeridos):
            return True

    camino.pop()
    visitado.remove((fila, columna))
    return False

def imprimir_laberinto(laberinto):
    """Imprime el laberinto"""
    for fila in laberinto:
        print(" ".join(map(str, fila)))

def imprimir_camino_en_laberinto(laberinto_original, camino):
    """
    Imprime el laberinto con el camino encontrado.
    'X' marca las celdas en el camino. 'I' y 'F' permanecen como tal.
    """
    laberinto_con_camino = copy.deepcopy(laberinto_original)
    for r, c in camino:
        if (r, c) != (8, 0) and (r, c) != (0, 0):
            laberinto_con_camino[r][c] = 'X'

    laberinto_con_camino[8][0] = 'I' # Inicio
    laberinto_con_camino[0][0] = 'F' # Fin

    for fila in laberinto_con_camino:
        print(" ".join(map(str, fila)))

datos_laberinto_original = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1]
]

laberinto_para_procesar = [
    [1 if celda in ['I', 'F'] else celda for celda in fila]
    for fila in datos_laberinto_original
]

fila_inicio, columna_inicio = 8, 0  
fila_fin, columna_fin = 0, 0     
puntos_minimos_requeridos = 23

camino_encontrado = []
celdas_visitadas = set()
puntos_iniciales = 0 

print("laberinto original:")
imprimir_laberinto(datos_laberinto_original)
print("\nintentando encontrar un camino...\n")

camino_valido_encontrado = resolver_laberinto(
    laberinto_para_procesar,
    fila_inicio,
    columna_inicio,
    camino_encontrado,
    puntos_iniciales,
    celdas_visitadas,
    fila_fin,
    columna_fin,
    puntos_minimos_requeridos
)

if camino_valido_encontrado:
    print("¡camino encontrado!")
    print("coordenadas del camino:", camino_encontrado)

    puntos_finales = 0
    for r, c in camino_encontrado:
        valor_celda = laberinto_para_procesar[r][c]
        if valor_celda in [3, 4]:
            puntos_finales += valor_celda
    print(f"Puntos totales acumulados: {puntos_finales}")

    print("\nlaberinto con la solucion del camino:")
    imprimir_camino_en_laberinto(datos_laberinto_original, camino_encontrado)
else:
    print("no se encontro un camino valido que cumpla con el minimo de 23 puntos.")
