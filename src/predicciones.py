from operacionesPredicciones import *


def prediccionSimple(k, sim):

    for u in range(len(matriz)):
        if matriz[u].count(None) != 0: # Se trata de un usuario para predecir
            kVecinos = []
            if u == 0: # Si el usuario para predecir un item es 0, se cogen como vecinos los sucesivos usuarios
                for j in range(1, k+1, 1):
                    kVecinos.append(j)
            elif u == len(matriz) - 1: # Si el usuario para predecir un item es el último, se cogen como vecinos los anteriores usuarios
                for j in range(len(matriz)-1, len(matriz)-1 - k, -1):
                    kVecinos.append(j)
            else:
                for j in range(k):
                    kVecinos.append(j-1)
                    kVecinos.append(j+1)
            
            for i in range(len(matriz[u])):
                if matriz[u][i] == None:
                    calcularPrediccionesSimple(u, i, kVecinos, sim)


def prediccionDiferenciaMedia(k, sim):

    global vecinos

    for u in range(len(matriz)):
        if matriz[u].count(None) != 0: # Se trata de un usuario para predecir
            kVecinos = []
            if u == 0: # Si el usuario para predecir un item es 0, se cogen como vecinos los sucesivos usuarios
                for j in range(1, k+1, 1):
                    kVecinos.append(j)
            elif u == len(matriz) - 1: # Si el usuario para predecir un item es el último, se cogen como vecinos los anteriores usuarios
                for j in range(len(matriz)-1, len(matriz)-1 - k, -1):
                    kVecinos.append(j)
            else:
                error = 0
                for j in range(u, u+k, 1):
                    if j >= len(matriz)-1:
                        error = k - len(kVecinos)
                        break
                    else:
                        kVecinos.append(j+1)

                if error != 0:
                    for j in range(u, u-error, -1):
                        kVecinos.append(j-1)

            vecinos.append((u, kVecinos))

            mediaU = calcularMedia(u)
            
            for i in range(len(matriz[u])):
                if matriz[u][i] == None:
                    calcularPrediccionesDiferenciaMedia(u, i, kVecinos, sim, mediaU)