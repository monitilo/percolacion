import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)

l=np.array([])
p=np.array([])
m=np.array([])
sigma=m


start=99638

index=np.arange(12,127,2)


for files in ls:

	if files.endswith(".txt"):
			
		f = open(files,"r")

		for j in range(0,start):
			f.readline()
		
		for h in index:

			l0=0
			p0=0
			p0sqr=0
			m0=0
			z=100000

			for j in range(0,z):

				aux=f.readline()
				aux=aux.split(";")
				l0=int(aux[0])
				p0=float(aux[1])+p0
				m0=float(aux[2])+m0
				p0sqr=float(aux[1])**2+p0sqr
			

			l=np.append(l,l0)
			p=np.append(p,p0/z)
			m=np.append(m,m0/z)
			sigma=np.append(sigma, p0sqr/z - (p0/z)**2)
			print "L = " + str(l0) + " , Z = " + str(z)
	

		f.close()
				

np.savetxt('lpmsigma.txt', [l,p,m,sigma], fmt='%1.6f', header='1:L;2:<P>;3:<M>;4:sigma')				
			
			
			
		
			
			
