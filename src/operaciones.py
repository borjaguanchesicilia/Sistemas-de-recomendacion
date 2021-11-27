from math import pow, sqrt

matriz = []; medias = []; similaridad = []; vecinos = []; predicciones = []


def lecturaFichero(nombreF):

    global matriz

    fichero = open(nombreF, 'r')
    valores = []
    linea = fichero.readline()
    
    while linea != "":
        for j in range(len(linea)):
            if linea[j] == "-":
                valores.append(None)
            elif linea[j] != " " and linea[j] != "\n":
                valores.append(int(linea[j]))
        matriz.append(valores); valores = []
        linea = fichero.readline()

    fichero.close()


def escrituraFichero():

    fichero = open("matrizResultado.txt", 'w')

    fichero.write("La matriz con los elementos faltantes es: \n\n")

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            fichero.write(str(matriz[i][j])+" ")
        fichero.write("\n")

    fichero.write("\n\nLa similaridad entre cada usuario es: \n\n")

    for i in range(len(similaridad)):
        fichero.write("Usuario: " + str(similaridad[i][0]) + "  Vecino: " + str(similaridad[i][1]) + " -->  " + str(similaridad[i][2]) + "\n")

    fichero.write("\n\nLos vecinos seleccionados para cada usuario son: \n\n")

    for i in range(len(vecinos)):
        fichero.write("Usuario: " + str(vecinos[i][0]) + " -->  " + str(vecinos[i][1]) + "\n")

    fichero.write("\n\nLas predicciones hechas han sido: \n\n")

    for i in range(len(predicciones)):
        fichero.write("Usuario: " + str(predicciones[i][0]) + "  Item: " + str(predicciones[i][1]) + "  Vecinos: " + str(predicciones[i][2]) + "  --> " + str(predicciones[i][3]) + "\n")

    fichero.close()