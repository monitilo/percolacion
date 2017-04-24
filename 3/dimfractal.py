import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)

l=np.array([])
p=np.array([])
m=np.array([])


start=99638

index=np.arange(12,127,2)


for files in ls:

	if files.endswith(".txt"):

		for h in index:
			
			f = open(files,"r")

			for j in range(0,start):
				f.readline()

			l0=0
			p0=0
			m0=0
			z=0
			
			for line in f:
		
				aux=line.split(";")
				l0=int(aux[0])
				if(l0==h):
					p0=float(aux[1])+p0
					m0=float(aux[2])+m0
					z=z+1
					

			l=np.append(l,h)
			p=np.append(p,p0/z)
			m=np.append(m,m0/z)
			print "L = " + str(h) + " , Z = " + str(z)
		
			"""i=0
			for line in f:
			
				if(i!=z):
				
					i=i+1
					aux=line.split(";")
					l0=int(aux[0])
					p0=float(aux[1])+p0
					m0=float(aux[2])+m0

				else:
					print l0
					i=0
					l=np.append(l,l0)
					p=np.append(p,p0/z)
					m=np.append(m,m0/z)
					aux=line.split(";")
					l0=int(aux[0])
					p0=float(aux[1])
					m0=float(aux[2])"""

			f.close()
				

np.savetxt('lpm.out1', [l,p,m], fmt='%1.6f', header='1:L;2:<P>;3:<M>')				
			
			
			
		
			
			
