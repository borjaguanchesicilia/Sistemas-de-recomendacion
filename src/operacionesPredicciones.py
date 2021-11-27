from operaciones import *


def calcularPrediccionesSimple(u, item, kVecinos, sim):

    sum1 = 0; sum2 = 0;

    for i in kVecinos:
        for j in range(len(sim)):
            if ((sim[j][0] ==u) and (sim[j][1] ==i)):
                sum1 += (sim[j][2] * matriz[i][item])
                sum2 += abs(sim[j][2])

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


def calcularPrediccionesDiferenciaMedia(u, item, kVecinos, sim, mediaU):

    sum1 = 0; sum2 = 0;

    for i in kVecinos:
        if matriz[i][item] != None:
            mediaV = calcularMedia(i)
            for j in range(len(sim)):
                if ((sim[j][0] == u) and (sim[j][1] == i)):
                    sum1 += round(sim[j][2] * (matriz[i][item] - mediaV), 2)
                    sum2 += round(abs(sim[j][2]), 2)

    prediccion = round(mediaU + (sum1 / sum2))

    predicciones.append((u, item, kVecinos, prediccion))

    matriz[u][item] = prediccion