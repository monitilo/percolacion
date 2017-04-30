import matplotlib.pyplot as plt
import sys
import numpy as np
import os
import scipy.stats as sp

cwd=os.getcwd()
ls=os.listdir(cwd)


for files in ls:

	if files.endswith(".txt"):

		
		l,p,m,sigma=np.loadtxt(files)
			
		x=np.log(l)
		y=np.log(m)
		
		ajus=sp.linregress(x,y)
		plt.plot(x,y,'ro')
		plt.plot(x,x*ajus[0]+ajus[1],label='$D = {i} \pm {j}$'.format(i=ajus[0],j=ajus[4]))
		plt.xlabel("ln(L)")
		plt.ylabel("ln(M)")
		plt.title("ln(M) vs ln(L)\n(Obtencion de la dimension fractal D)")
		plt.legend(loc='best')
		plt.savefig("dimfractal.png")
		plt.show()
		
		

		
		

