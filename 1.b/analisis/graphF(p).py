import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)

for files in ls:

	if files.endswith(".txt"):

		f = open(files,"r") 

		aux=f.readline()
		aux=aux.split(",")
		l=aux[0]
		l=int(l[7:len(l)])
		z=aux[1]
		z=z.split(" ")
		z=int(z[3])
		f.readline()
		p=np.array([])
		F=np.array([])

		for line in f:

			aux=line.split(";")
			p=np.append(p,float(aux[0]))
			F=np.append(F,float(aux[1])/z)

		i=0
		while(F[i]<0.5):
			i=i+1
		pc=p[i]
		print "L = " + str(l) + " pc = " + str(pc)
		plt.plot(p,F, label='$L = {i}; pc = {h}$'.format(i=l,h=pc))

plt.legend(loc='best')
plt.plot([0,1],[0.5,0.5])
plt.xlabel("p")
plt.ylabel("F(p)")
plt.title("Distribucion de probabilidad F(p)")
plt.show()



