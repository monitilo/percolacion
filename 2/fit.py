import matplotlib.pyplot as plt
import sys
import numpy as np
import scipy.stats as sp
import os

def ajuste(x,y,inf,up):

	xfit=np.array([])
	yfit=xfit
	i=0

	while(x[i] <= inf):
		i=i+1

	while(x[i] <= up):
		xfit=np.append(xfit,x[i])
		yfit=np.append(yfit,y[i])
		i=i+1

	p=sp.linregress(xfit,yfit)
	plt.plot(xfit,yfit,'go',xfit,xfit*p[0]+p[1])
	plt.xlabel("p")
	plt.ylabel(r"\P_inf")
	plt.title("Fuerza de cluster percolante P_inf")
	plt.show()
	return p

cwd=os.getcwd()
ls=os.listdir(cwd)
x=np.array([])
y=x

for files in ls:
	if files.endswith(".out"):

		f = open(files,"r") 

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
		
		"""th=0.00001
		j=0
		while pinf[j] <= th:
			j = j + 1
		pc=p[j]
		print pc"""

		
		j=0
		pc=0.5927

		while p[j] <= pc:
			j = j + 1
		

		for i in range(j,len(pinf)):

			if pinf[i]!=0:

				y=np.append(y,np.log(pinf[i]))
				x=np.append(x,np.log(np.abs(p[i]-pc)))
				
		plt.figure(1)
		plt.plot(p,pinf,'ro')
		plt.show()
		plt.figure(2)
		plt.plot(x,y,'ro')
		plt.show()
		plt.figure(3)
		inf=-10
		up=-7
		aj=ajuste(x,y,inf,up)
		print aj





