from operaciones import *


def calcularPrediccionesSimple(u, item, kVecinos):

    sum1 = 0; sum2 = 0;

    for i in kVecinos:
        if matriz[i['vecino']][item] != None:
            sum1 += round(i['sim'] * (matriz[i['vecino']][item]), 2)
            sum2 += i['sim']

    prediccion = round(sum1 / sum2)

    predicciones.append((u, item, kVecinos, prediccion))

    matriz[u][item] = prediccion


def calcularMedia(usuario):

    sum = 0; cont = 0
    
    for i in range(len(matriz[usuario])):
        if matriz[usuario][i] != None:
            sum += matriz[usuario][i]
        else:
            cont += 1

    if cont == 0:
        return round(sum / len(matriz[usuario]), 2)

    else:
        return round(sum / (len(matriz[usuario]) - cont), 2)


def calcularPrediccionesDiferenciaMedia(u, item, kVecinos, mediaU):

    sum1 = 0; sum2 = 0;

    for i in kVecinos:
        if matriz[i['vecino']][item] != None:
            mediaV = calcularMedia(i['vecino'])
            sum1 += round(i['sim'] * (matriz[i['vecino']][item] - mediaV), 2)
            sum2 += i['sim']

    prediccion = round(mediaU + (sum1 / sum2))

    predicciones.append((u, item, kVecinos, prediccion))

    matriz[u][item] = prediccion