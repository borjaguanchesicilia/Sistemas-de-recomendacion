# Sistemas de recomendación:

### Información de uso:

* En primer lugar, se tiene que tener una matriz donde se represente en las filas los ***usuarios***, y en las columnas los ***items*** (lo que los usuarios valoran). La matriz tiene que ser como la que se muestra a continuación:

					5 3 4 4 -

					3 1 2 3 3

					4 3 4 3 5

					3 3 1 5 4

					1 5 5 2 1
	* Donde cada valor representa la valoración que le ha dado un usuario a un item. El símbolo de - representa a un usuario que no ha valorado ese item, y que debe de ser predecido.

* Se debe de elegir una **métrica a utilizar**. En este caso se han implementado 3:

	* ***Correlación de Pearson*** (1).
	
	* ***Distancia coseno*** (2).
	
	* ***Distancia Euclídea*** (3).


* A continuación, se tiene que elegir el **número de vecinos** que serán considerados. Cabe destacar que, el número de vecinos no puede ser menor que 3 ni obviamente mayor que el número de usuarios que hayan.


* Y por último, se tiene que elegir un **modo de predicción**. En este caso se han implementado 2 modos:

	* ***Predicción simple*** (1).
	
	* ***Diferencia con la media*** (2).


#### Ejemplo de uso:

* Nos encontramos en un directorio, donde existe el fichero matriz.txt, y en él tenemos por ejemplo la matriz que se mostró anteriormente. 

			python3.6 main.py matriz.txt 1 3 2
        
    * **1:** Es el segundo argumento, indica la métrica a utilizar, que como se indicó anteriormente puede ser: ***Correlación de Pearson (1)***, ***Distancia coseno (2)***, ***Distancia Euclídea (3)***.
    
    * **3:** Es el tercer argumento, indica el número de vecinos a considerar.
    
    * **2:** Es el cuarto argumento, indica el modo de predicción a utilizar, que como se indicó anteriormente puede ser: ***Predicción simple (1)***, ***Diferencia con la media (2)***.


### Datos sobre el código:

* Fichero ***main.py***: Contiene la invocación de la función principal, donde antes de proceder a realizar los cálculos, se comprueba que todos los parámetros introducidos son correctos.

* Fichero ***operaciones.py***: Contiene la función para la lectura del fichero de entrada con la matriz de utilidades y la funión de escritura con todos los resultados.

* Fichero ***metricas.py***: Contiene las funciones que invocan a otras funciones encargadas de realizar los cálculos de las distintas métricas para cada uno de los usuarios.

* Fichero ***operacionesMetricas.py***: Contiene las funciones de cálculo para cada una de las métricas.

* Fichero ***predicciones.py***: Contiene las funciones que invocan a otras funciones encargadas de realizar los cálculos de las distintas predicciones para cada uno de los items/usuarios.

* Fichero ***operacionesPredicciones.py***: Contiene las funciones de cálculo para cada los dos modos de predicción.
