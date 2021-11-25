from operaciones import *


def correlacionPearson():

    similitud = []

    for u in range(len(matriz)):
        if (u == 0):
            inicio = 1
        else:
            inicio = 0
        for v in range(inicio, len(matriz), 1):
            similitud.append((u, v, calcularCorrelacionPearson(u, v)))

    print("Correlación de Pearson: \n", similitud, "\n\n")


def distanciaCoseno():

    similitud = []

    for u in range(len(matriz)):
        if (u == 0):
            inicio = 1
        else:
            inicio = 0
        for v in range(inicio, len(matriz), 1):
            similitud.append((u, v, calcularDistanciaCoseno(u, v)))

    print("Distancia coseno: \n", similitud, "\n\n")


def distanciaEuclidea():

    similitud = []

    for u in range(len(matriz)):
        if (u == 0):
            inicio = 1
        else:
            inicio = 0
        for v in range(inicio, len(matriz), 1):
            similitud.append((u, v, calcularDistanciaEuclidea(u, v)))

    print("Distancia Euclidea: \n", similitud, "\n\n")