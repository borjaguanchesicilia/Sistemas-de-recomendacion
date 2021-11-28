from operacionesPredicciones import *


def prediccionSimple(k, sim):

    for u in range(len(matriz)):
        if matriz[u].count(None) != 0: # Se trata de un usuario para predecir
            kVecinos = []
            cont = 0
            for i in sim:
                if cont == k:
                    break
                elif i['usuario'] == u:
                    kVecinos.append(i)
                    cont += 1

            vecinos.append((u, kVecinos))
            
            for i in range(len(matriz[u])):
                if matriz[u][i] == None:
                    calcularPrediccionesSimple(u, i, kVecinos)


def prediccionDiferenciaMedia(k, sim):

    global vecinos

    for u in range(len(matriz)):
        if matriz[u].count(None) != 0: # Se trata de un usuario para predecir
            kVecinos = []
            cont = 0
            for i in sim:
                if cont == k:
                    break
                elif i['usuario'] == u:
                    kVecinos.append(i)
                    cont += 1

            vecinos.append((u, kVecinos))

            mediaU = calcularMedia(u)
            
            for i in range(len(matriz[u])):
                if matriz[u][i] == None:
                    calcularPrediccionesDiferenciaMedia(u, i, kVecinos, mediaU)