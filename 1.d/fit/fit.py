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
	#plt.plot(xfit,yfit,'ro',xfit,xfit*p[0]+p[1])
	plt.xlabel("ln(s)")
	plt.ylabel("ln(ns)")
	#plt.show()
	return p

cwd=os.getcwd()
ls=os.listdir(cwd)
r=[]
tau=[]
p=[]

for files in ls:
	if files.endswith(".txt"):

		f = open(files,"r") 

		aux=f.readline()
		aux=aux.split(",")
		aux=aux[1]
		aux=aux.split(" ")
		p.append(float(aux[3]))
		
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

		#plt.figure()
		#plt.plot(x,y,'go')
		

		inf=3
		up=6
		aj=ajuste(x,y,inf,up)
		tau.append(-aj[0])
		r.append(aj[2]**2)

maxr=np.amax(r)

i=0

while r[i]!=maxr:
	i=i+1

print "P = " + str(p[i]) + ", Tau = " + str(tau[i]) + " R^2 = " + str(r[i])





