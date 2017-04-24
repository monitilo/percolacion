import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)


for files in ls:

	if files.endswith(".txt"):

		
		l,p,m=np.loadtxt(files)
			
		x=np.log(l)
		y=np.log(m)
		
		ajus=np.polyfit(x,y,1)
		plt.plot(x,y,'ro')
		plt.plot(x,x*ajus[0]+ajus[1],label='$D = {i}$'.format(i=ajus[0]))
		plt.xlabel("ln(L)")
		plt.ylabel("ln(M)")
		plt.title("ln(M) vs ln(L)\n(Obtencion de la dimension fractal D)")
		plt.legend(loc='best')
		plt.savefig("dimfractal.png")
		plt.show()
		
		

		
		

