1.b:
percolacion1b.c es un programa que corre el algoritmo de Hoshen-Kopelman, para un p y un L que se dan como argumentos al ejecutable, 27000 veces y le permite tener estadistica del mismo. Por un lado obtiene un archivo con la distribucion de fragmentos promedio ns(p,L), y por otro, un archivo que registra p, cuantas veces percolo de las 27000 y el valor medio del tamaño del fragmento percolante.

Las reglas para compilar percolacion1b.c son "gcc percolacion1b.c -Wall -O3 -o test.e"

run.sh simplemente es un script de bash que corre el programa para un rango de p's y L's y va guardando los datos obtenidos en carpetas correspondientes a cada L.

En la carpeta "analisis", el script graphF(p).py grafica la probabilidad acumulativa para cada L.

