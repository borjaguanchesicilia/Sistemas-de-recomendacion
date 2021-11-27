import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--f', type=str, help="Nombre fichero de entrada")
parser.add_argument('--m', type=int, help="Métrica a utilizar: 1 --> Correlación de Pearson; 2 --> Correlación coseno; 3 --> Distancia Euclídea")
parser.add_argument('--k', type=int, help="Nº de vecinos a utilizar (K < tamaño de la matriz)")
parser.add_argument('--p', type=int, help="Predicción a utilizar: 1 --> Predicción simple; 2 --> Diferencia con la media")
print(parser.parse_args(sys.argv[1:]))

print(sys.argv[1])