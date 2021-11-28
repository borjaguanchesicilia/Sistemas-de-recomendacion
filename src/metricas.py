from operacionesMetricas import *


def correlacionPearson():

    similitud = []

    for u in range(len(matriz)):
        if (u == 0):
            inicio = 1
        else:
            inicio = 0
        for v in range(inicio, len(matriz), 1):
            if (u != v):
                similitud.append({'usuario': u, 'vecino': v, 'sim': calcularCorrelacionPearson(u, v)})

    return similitud


def distanciaCoseno():

    similitud = []

    for u in range(len(matriz)):
        if (u == 0):
            inicio = 1
        else:
            inicio = 0
        for v in range(inicio, len(matriz), 1):
            similitud.append((u, v, calcularDistanciaCoseno(u, v)))

    return similitud


def distanciaEuclidea():

    similitud = []

    for u in range(len(matriz)):
        if (u == 0):
            inicio = 1
        else:
            inicio = 0
        for v in range(inicio, len(matriz), 1):
            similitud.append((u, v, calcularDistanciaEuclidea(u, v)))

    return similitud