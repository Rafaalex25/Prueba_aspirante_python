# Prueba_aspirante_python


el proyecto consta de una carpeta llamda tiendas el cual es el proyeto hecho en django, y el archivo llamado teoria 

### el problema planteado es el siguente 

El objetivo es minimizar el tiempo que tardan en llegar del primer centro comercial N con peces vendidos k colectados por cada centro comercial.

### solucion ############################## 

Se realizo un programa para entender y dar solucion al problema de nombre teoria.py


Se usa el algortimo de Dijkstra es un algortimo que permiete encontrar el camino de coste minimo desde un nodo origen a todos los
demas nodos del grafo.

Segundo no se considera los tipos de pescados y estos repartidos por cada tienda de los centros comerciales, con el fin de reducir la complejidad del problema.

Los siguentes pasos mostrados a continuacion explican el funcionamiento del algoritmo en el programa teoria.py

1. Asignar a cada nodo una distancia tentativa: 0 para el nodo inicial e infinito para todos los nodos restantes. Predecesor nulo para todos.
2. Establecer al nodo inicial como nodo actual y crear un conjunto de nodos no visitados.
3. Para el nodo actual, considerar a todos sus vecinos no visitados con peso w.
	a) Si la distancia del nodo actual sumada al peso w es menor que la distancia tentativa actual de ese vecino,
	   sobreescribir la distancia con la suma obtenida y guardar al nodo actual como predecesor del vecino
4. Cuando se termina de revisar a todos los vecino del nodo actual, se marca como visitado y se elimina del conjunto no  visitado.
5. Continúa la ejecución hasta vaciar al conjunto no visitado.
6. Seleccionar el nodo no visitado con menor distancia tentativa y marcarlo como el nuevo nodo actual.

########################################## Carpeta tiendas ##########################

En esta carpeta contiene el projecto desarrolado en django, usando una base de datos sql3lite, la app contiene un formulario de los centros comerciales asi como la distancia para que el usuario llene los campos,
en la carpeta templete condiene los html usados para el login, y el formulario



#################3 que haria falta ##############################
 una vez de llenar la base de datos con la informacion de los centros comerciales y la distanca entre un centro comercial a otro , 
implementar el codigo de teoria.py usando un metodo get para leer y el algortimo calcule la distancia 
minimima entre centros comerciales, una vez realizado, seria considerar la lista de pescados vendidos por cada centro comercial,  
