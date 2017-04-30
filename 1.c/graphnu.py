import matplotlib.pyplot as plt
import sys
import numpy as np
import os
import scipy.stats as sp

cwd=os.getcwd()
ls=os.listdir(cwd)

def swap(x,i,j):

	aux=x[i]
	x[i]=x[j]
	x[j]=aux

def sort(x,y):

	for i in range(0,len(x)):

		for j in range(0,len(x)):

			if(x[i]<x[j]):
		
				swap(x,i,j)
				swap(y,i,j)

for files in ls:

	if files.endswith(".txt"):

		
		l,p,m,sigma=np.loadtxt(files)
			
		x=np.log(l)
		y=np.log(np.sqrt(sigma))
		
		ajus=sp.linregress(x,y)
		plt.subplot(211)
		plt.plot(x,y,'ro')
		plt.plot(x,x*ajus[0]+ajus[1],label=r'$\nu = {i} $'.format(i=-1/ajus[0]))
		plt.xlabel("ln(L)")
		plt.ylabel("ln($\sigma$)")
		plt.title(r"ln($\sigma$) vs ln(L)(Obtencion del coeficiente $\nu)$")
		plt.legend(loc='best')

		plt.subplot(212)


		sort(sigma,p)
		
		i=np.where(sigma<0.00065)
		i=i[0]
		i=i[len(i)-1]+1
		ajus=sp.linregress(sigma[0:i],p[0:i])
		plt.plot(sigma,p,'ro')
		plt.plot(sigma[0:i],sigma[0:i]*ajus[0]+ajus[1],label=r'$ p_c(\infty) = {i}$'"\n" r'$\beta = {j} $'.format(i=ajus[1],j=ajus[0]))
		plt.xlabel("$\sigma$")
		plt.ylabel("$p_c(L)$")
		plt.title("$p_c(L)$ vs $\sigma$ (Obtencion de $p_c(\infty)$")
		plt.legend(loc='best')
		
		plt.savefig("nu y pcinf" + " L=" + str(l[-1]) + ".png")
		plt.show()
		
		

		
		

