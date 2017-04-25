import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)

p=np.array([])
m2=np.array([])

for files in ls:

	if files.endswith(".txt"):
		
		f=open(files,"r")
		
		f.readline()
		f.readline()
		
		for line in f:
			
			aux=line.split(";")
			p=np.append(p,float(aux[0]))
			m2=np.append(m2,float(aux[1]))
			

		plt.plot(p,m2,'ro')
		plt.show()
