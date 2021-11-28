from operaciones import *


def calcularMedia(calificacionesU, calificacionesV, n):

    sum = 0
    if (n == 0):
        valPredecir = calificacionesU.count(None); n = len(calificacionesU) - valPredecir

    for i in range(len(calificacionesU)):
        if ((calificacionesU[i] != None) and (calificacionesV[i] != None)):
            sum += calificacionesU[i]

    return (sum / n, n)


def calcularCorrelacionPearson(u, v):

    global matriz; global similaridad

    mediaU = calcularMedia(matriz[u], matriz[v], 0)
    mediaV = calcularMedia(matriz[v], matriz[u], mediaU[1])

    sum1 = 0; sum2 = 0; sum3 = 0

    for i in range(len(matriz[u])):
        calificacionU = matriz[u][i]; calificacionV = matriz[v][i]
        if ((calificacionU != None) and (calificacionV != None)):
            sum1 += (calificacionU - mediaU[0]) * (calificacionV - mediaV[0])
            sum2 += pow((calificacionU - mediaU[0]), 2)
            sum3 += pow((calificacionV - mediaV[0]), 2)

    correlacion = round((sum1 / (sqrt(sum2) * sqrt(sum3))), 2)

    similaridad.append((u, v, correlacion))

    return correlacion


def calcularDistanciaCoseno(u, v):

    global matriz; global similaridad

    sum1 = 0; sum2 = 0; sum3 = 0

    for i in range(len(matriz[u])):
        calificacionU = matriz[u][i]; calificacionV = matriz[v][i]
        if ((calificacionU != None) and (calificacionV != None)):
            sum1 += calificacionU * calificacionV
            sum2 += pow(calificacionU, 2)
            sum3 += pow(calificacionV, 2)

    distancia = round((sum1 / (sqrt(sum2) * sqrt(sum3))), 2)

    similaridad.append((u, v, distancia))

    return distancia


def calcularDistanciaEuclidea(u, v):

    global matriz; global similaridad

    sum = 0

    for i in range(len(matriz[u])):
        calificacionU = matriz[u][i]; calificacionV = matriz[v][i]
        if ((calificacionU != None) and (calificacionV != None)):
            sum += pow((calificacionU - calificacionV), 2)

    distancia = round(sqrt(sum))

    similaridad.append((u, v, distancia))

    return distancia


def ordenar(val):
    return val['sim']


def normalizar(sim):

    simNormalizadas = []

    for i in sim:
        if i['sim'] < 0:
            val = {'usuario': i['usuario'], 'vecino': i['vecino'], 'sim': round(((i['sim']-(-1)) / (1-(-1))), 2)}
            simNormalizadas.append(val)
        else:
            simNormalizadas.append(i)

    return simNormalizadas