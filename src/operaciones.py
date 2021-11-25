from math import pow, sqrt

matriz = []; medias = []


def calcularMedia(calificacionesU, calificacionesV, n):

    sum = 0
    if (n == 0):
        ceros = calificacionesU.count(0); n = len(calificacionesU) - ceros

    for i in range(len(calificacionesU)):
        if ((calificacionesU[i] != 0) and (calificacionesV[i] != 0)):
            sum += calificacionesU[i]

    return (sum / n, n)


def funcionPearson(valorItem, media, expo):

    return pow((valorItem - media), expo)


def calcularCorrelacionPearson(u, v):

    global matriz

    mediaU = calcularMedia(matriz[u], matriz[v], 0)
    mediaV = calcularMedia(matriz[v], matriz[u], mediaU[1])

    print(mediaU, mediaV)

    sum1 = 0; sum2 = 0; sum3 = 0

    for i in range(len(matriz[u])):
        calificacionU = matriz[u][i]; calificacionV = matriz[v][i]
        if ((calificacionU != 0) and (calificacionV != 0)):
            sum1 += funcionPearson(calificacionU, mediaU[0], 1) * funcionPearson(calificacionV, mediaV[0], 1)
            sum2 += funcionPearson(calificacionU, mediaU[0], 2)
            sum3 += funcionPearson(calificacionV, mediaV[0], 2)

    return round((sum1 / (sqrt(sum2) * sqrt(sum3))), 2)


def calcularDistanciaCoseno(u, v):

    global matriz

    sum1 = 0; sum2 = 0; sum3 = 0

    for i in range(len(matriz[u])):
        calificacionU = matriz[u][i]; calificacionV = matriz[v][i]
        if ((calificacionU != 0) and (calificacionV != 0)):
            sum1 += calificacionU * calificacionV
            sum2 += pow(calificacionU, 2)
            sum3 += pow(calificacionV, 2)

    return round((sum1 / (sqrt(sum2) * sqrt(sum3))), 2)


def calcularDistanciaEuclidea(u, v):

    global matriz

    sum = 0

    for i in range(len(matriz[u])):
        calificacionU = matriz[u][i]; calificacionV = matriz[v][i]
        if ((calificacionU != 0) and (calificacionV != 0)):
            sum += pow((calificacionU - calificacionV), 2)

    return round(sqrt(sum))