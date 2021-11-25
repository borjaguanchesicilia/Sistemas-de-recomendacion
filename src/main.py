import sys
from metricas import *


def lecturaFichero(nombreF):

    global matriz

    fichero = open(nombreF, 'r')
    valores = []
    linea = fichero.readline()
    
    while linea != "":
        for j in range(len(linea)):
            if linea[j] == "-":
                valores.append(0)
            elif linea[j] != " " and linea[j] != "\n":
                valores.append(int(linea[j]))
        matriz.append(valores); valores = []
        linea = fichero.readline()


def inicializar():

    try:
        nombreF = sys.argv[1]; metrica = int(sys.argv[2]); nVecinos = sys.argv[3]; prediccion = int(sys.argv[4])
    except:
        print("ERROR: Debe introducir los cuatro argumentos.")
    else:
        try:
            f = open(nombreF, 'r')
        except:
            print("ERROR: El fichero no existe")
        else:
            try:
                assert(metrica == 1 or metrica == 2 or metrica == 3)
            except:
                print("ERROR: Seleccione una métrica válida.")
            else:
                try:
                    assert(nVecinos.isdigit())
                except:
                    print("ERROR: Seleccione un número de vecinos válido.")
                else:
                    try:
                        assert(prediccion == 1 or prediccion == 2)
                    except:
                        print("ERROR: Seleccione una método de predicción válido.")
                    else:
                        try:
                            lecturaFichero(nombreF)
                        except:
                            print("ERROR: En el formato del fichero.")
                        else:
                            operacionMedia()
                            correlacionPearson()
                            distanciaCoseno()
                            distanciaEuclidea()
    

if __name__ == "__main__":
    inicializar()