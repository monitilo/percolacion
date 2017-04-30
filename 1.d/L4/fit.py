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
	#plt.xlabel("ln(s)")
	#plt.ylabel("ln(ns)")
	#plt.show()
	return p

cwd=os.getcwd()
ls=os.listdir(cwd)
r=[]
tau=[]
p=[]
ordenada=[]
rmayor=0

for files in ls:
	if files.endswith(".txt"):

		f = open(files,"r") 

		aux=f.readline()
		aux1=aux.split(",")
		aux1=aux1[1]
		aux1=aux1.split(" ")
		p.append(float(aux1[-1]))
		print float(aux1[-1])
		aux2=aux.split(",")
		aux2=aux2[0]
		aux2=aux2.split(" ")
		l=int(aux2[-1])
		
		f.readline()
		ns=np.array([])
		x=np.array([])
		y=np.array([])

		for line in f:

			aux=line.split(";")
			ns=np.append(ns,float(aux[1]))

		#norm=np.sum(ns)

		for i in xrange(0,len(ns)):
	
			if(ns[i]!=0):
	
				y=np.append(y,np.log(ns[i]))
				x=np.append(x,np.log(i+1))

		#plt.figure()
		#plt.plot(x,y,'go')
		

		inf=0
		up=2
		aj=ajuste(x,y,inf,up)
		tau.append(-aj[0])
		ordenada.append(aj[1])
		r.append(aj[2]**2)

		if(aj[2]**2>rmayor):

			xfinal=x
			yfinal=y
			rmayor=aj[2]**2

maxr=np.amax(r)

i=0

while r[i]!=maxr:
	i=i+1

plt.plot(xfinal,yfinal,'go')
plt.plot([inf,up],[-tau[i]*inf+ordenada[i],-tau[i]*up+ordenada[i]],'r',label="Tau = {e} \n $p_c(L = {h})$ = {j} \n $R^2$ = {k}".format(e=tau[i],j=p[i],k=r[i],h=l))
plt.xlabel("ln(s)")
plt.ylabel("ln($n_s$)")
plt.title("Ajuste de la distribucion de fragmentos para L = " + str(l) +"\n(Obtencion de Tau)")
plt.legend(loc='best')
plt.savefig("tau"+ str(l)+ ".png")
plt.show()





