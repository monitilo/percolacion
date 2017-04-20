import matplotlib.pyplot as plt
import sys
import numpy as np
import os

def ajuste(x,y,cut):

	xfit=np.array([])
	yfit=np.array([])
	i=0

	while(x[i]<=cut):

		xfit=np.append(xfit,x[i])
		yfit=np.append(yfit,y[i])
		i=i+1 

	plt.plot(xfit,yfit,'ro')
	p=np.polyfit(xfit,yfit,1)
	plt.plot(xfit,xfit*p[0]+p[1])
	plt.show(block=True)
	return p

cwd=os.getcwd()
ls=os.listdir(cwd)

for files in ls:
	if files.endswith(".txt"):

		f = open(files,"r") 

		f.readline()
		f.readline()
		ns=np.array([])
		x=np.array([])
		y=np.array([])

		for line in f:

			aux=line.split(";")
			ns=np.append(ns,float(aux[1]))

		norm=np.sum(ns)

		for i in xrange(0,len(ns)):
	
			if(ns[i]!=0):
	
				y=np.append(y,np.log(ns[i]/norm))
				x=np.append(x,np.log(i+1))

		plt.plot(x,y,'go')

		p=ajuste(x,y,5.6)

		print p



