from math import pow, sqrt

matriz = []; medias = []


def operacionMedia():

    global medias

    [medias.append(calcularMedia(i)) for i in matriz]
        


def calcularMedia(usuario):

    sum = 0; cont = 0
    for j in usuario:
        if j == 0:
            cont += 1
        else:
            sum += j
    
    return (sum / (len(usuario) - cont))


def funcionPearson(valorItem, media, expo):

    return pow((valorItem - media), expo)


def calcularCorrelacionPearson(u, v):

    global matriz

    sum1 = 0; sum2 = 0; sum3 = 0

    for i in range(len(matriz[u])):
        calificacionU = matriz[u][i]; calificacionV = matriz[v][i]
        if ((calificacionU != 0) and (calificacionV != 0)):
            sum1 += funcionPearson(calificacionU, medias[u], 1) * funcionPearson(calificacionV, medias[v], 1)
            sum2 += funcionPearson(calificacionU, medias[u], 2)
            sum3 += funcionPearson(calificacionV, medias[v], 2)

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