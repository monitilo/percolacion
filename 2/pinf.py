import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)

for files in ls:

	if files.endswith(".txt"):

		f = open(files,"r") 

		l=f.readline()
		l=l.split(",")
		l=l[0]
		l=int(l[7:len(l)])
		f.readline()
		pinf=np.array([])
		p=np.array([])

		for line in f:

			aux=line.split(";")
			p=np.append(p,float(aux[0]))
			if(float(aux[2])!=0):
				pinf=np.append(pinf,float(aux[2])/(27000*l*l))
			else:
				pinf=np.append(pinf,0)


		plt.plot(p,pinf,'o', label='$L = {i}$'.format(i=l))
		"""plt.title("L = " + str(l))
		plt.show()"""

plt.legend(loc='best')
plt.xlabel("p")
plt.ylabel(r"\P_inf")
plt.title("Fuerza de cluster percolante P_inf")
plt.show()



