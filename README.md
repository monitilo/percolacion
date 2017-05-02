-)1.a:
percolacion1a.c es un programa que corre el algoritmo de Hoshen-Kopelman y cambia la probabilidad en función de si percolo o no. Los datos se guardan en un archivo de texto donde se guarda la probabilidad de cada repeticion para luego hallar el valor medio.
Las reglas para compilar percolacion1a.c son "gcc percolacion1b.c -Wall -O3 -o test.e"

-)1.b:
percolacion1b.c es un programa que corre el algoritmo de Hoshen-Kopelman, para un p y un L que se dan como argumentos al ejecutable, 27000 veces y le permite tener estadistica del mismo. Por un lado obtiene un archivo con la distribucion de fragmentos promedio ns(p,L), y por otro, un archivo que registra p, cuantas veces percolo de las 27000 y el valor medio del tamaño del fragmento percolante.

Las reglas para compilar percolacion1b.c son "gcc percolacion1b.c -Wall -O3 -o test.e"

run.sh simplemente es un script de bash que corre el programa para un rango de p's y L's y va guardando los datos obtenidos en carpetas correspondientes a cada L.

En la carpeta "analisis", el script graphF(p).py grafica la probabilidad acumulativa para cada L.

-)1.c:

Corriendo el programa percolacion1a.c con mas valores de L (12:2:126), se obtuvieron los datos necesarios para poder graficar la sigma vs L y poder hallar nu,beta y pc(inf) utilizando el script graphnu.py

-)1.d:
Con las ns halladas en 1.b, se corrio un script de fitteo (fit.py) para ns cerca de la probabilidad critica hallada en 1.a para ver cual ajusta mejor con una recta para ln(ns) vs ln(s). El que mejor ajuste es el de la pc.

-)2:
Con los datos hallados en 1.b, se grafica la fuerza de cluster percolante con pinf.py.

fitpc.py fittea los datos para hallar beta a partir de una pc dada.
fitth.py fittea los datos para hallar beta a partir de un umbral dado.

-)3:
A partir de los datos obtenidos en 1.c se calcula la dimension fractal D mediante el uso del script graph.d

dimfractal.py y dimfractal2.py son scripts auxiliares para poder transformar los datos de 1.c en cosas mas amigables.

-)4:
Utilizando los datos de ns sin percolantes guardados en 6, e4.py realiza los calculos pertinentes para graficar F(z) vs z. y guarda un archivo.out con los valores donde F(z) alcanza el maximo para cada s y p

-)5:
Cargando el archivo.out guardado en el punto 4, se procede a graficarlos y ajustarlos en e5.py

-)6:

percolacion6.c hace lo mismo que percolacion1b.c salvo que guarda los ns SIN percolantes. 
run.sh es igual al run.sh de 1.b.
momento2.py es un script auxiliar que calcula el m2(p) de los datos de las ns que arroja percolacion6.c
graphgamma.py es el script encargado de realizar el gamma-matching.
sort.py es un script auxiliar que ordena vectores de menor a mayor.

