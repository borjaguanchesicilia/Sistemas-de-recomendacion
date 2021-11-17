import sys

def inicializar():

    try:
        matriz = sys.argv[1]; metrica = int(sys.argv[2]); nVecinos = sys.argv[3]; prediccion = int(sys.argv[4])
    except:
        print("ERROR: Debe introducir los cuatro argumentos.")

    try:
        f = open(matriz, 'r')
    except:
        print("ERROR: El fichero no existe")

    try:
        assert(metrica == 1 or metrica == 2 or metrica == 3)
    except:
        print("ERROR: Seleccione una métrica válida.")

    try:
        assert(nVecinos.isdigit())
    except:
        print("ERROR: Seleccione un número de vecinos válido.")

    try:
        assert(prediccion == 1 or prediccion == 2)
    except:
        print("ERROR: Seleccione una método de predicción válido.")
    

if __name__ == "__main__":
    inicializar()