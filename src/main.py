import argparse
import sys
from metricas import *
from predicciones import *


def inicializar():

    try:
        nombreF = sys.argv[1]; metrica = sys.argv[2]; nVecinos = sys.argv[3]; prediccion = sys.argv[4]
    except:
        print("ERROR: Debe introducir los cuatro argumentos.")
    else:
        try:
            open(nombreF, 'r')
        except:
            print("ERROR: El fichero no existe")
        else:
            try:
                assert(metrica.isdigit())
                metrica = int(metrica); assert(metrica == 1 or metrica == 2 or metrica == 3)
            except:
                print("ERROR: Seleccione una métrica válida.")
            else:
                try:
                    assert(nVecinos.isdigit())
                    nVecinos = int(nVecinos); assert(nVecinos >= 3)
                except:
                    print("ERROR: Seleccione un número de vecinos válido.")
                else:
                    try:
                        assert(prediccion.isdigit())
                        prediccion = int(prediccion); assert(prediccion == 1 or prediccion == 2)
                    except:
                        print("ERROR: Seleccione una método de predicción válido.")
                    else:
                        try:
                            lecturaFichero(nombreF)
                        except:
                            print("ERROR: En el formato del fichero.")
                        else:
                            try:
                                assert(nVecinos < len(matriz))
                            except:
                                print("ERROR: No puede seleccionar tantos vecinos")
                            else:
                                try:
                                    if metrica == 1:
                                        sim = correlacionPearson()
                                    elif metrica == 2:
                                        sim = distanciaCoseno()
                                    elif metrica == 3:
                                        sim = distanciaEuclidea()

                                    sim.sort(key=ordenar)
                                    sim.reverse()

                                    if metrica == 1:
                                        sim = normalizar(sim)
                                    
                                except:
                                    print("ERROR: Se produjo un error en el cálculo de la métrica")
                                else:
                                    try:
                                        if prediccion == 1:
                                            prediccionSimple(nVecinos, sim)
                                        elif prediccion == 2: 
                                            prediccionDiferenciaMedia(nVecinos, sim)
                                    except:
                                        print("ERROR: Se produjo un error en el cálculo de la predicción")
                                    else:
                                        escrituraFichero()
                                        print("OK: El resultado se encuentra en el fichero matrizResultado.txt.")

if __name__ == "__main__":
    inicializar()