import matplotlib.pyplot as plt
import sys
import numpy as np
import scipy.stats as sp
import os

def confint(x, y, prob=0.95):
	 
	x = np.array(x)
	y = np.array(y)
	n = len(x)
	xy = x * y
	xx = x * x

	# estimates
	b1 = (xy.mean() - x.mean() * y.mean()) / (xx.mean() - x.mean()**2)
	b0 = y.mean() - b1 * x.mean()
	s2 = 1./n * sum([(y[i] - b0 - b1 * x[i])**2 for i in xrange(n)])
		
	#confidence intervals
		
	alpha = 1 - prob
	c1 = sp.chi2.ppf(alpha/2.,n-2)
	c2 = sp.chi2.ppf(1-alpha/2.,n-2)
		
	c = -1 * sp.t.ppf(alpha/2.,n-2)
	bb1 = c * (s2 / ((n-2) * (xx.mean() - (x.mean())**2)))**.5

	bb0 = c * ((s2 / (n-2)) * (1 + (x.mean())**2 / (xx.mean() - (x.mean())**2)))**.5

	return [bb1,bb0]


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
	p=np.append(p,confint(xfit,yfit))
	#plt.plot(xfit,yfit,'ro',xfit,xfit*p[0]+p[1])
	#plt.xlabel("ln(s)")
	#plt.ylabel("ln(ns)")
	#plt.show()
	return p

cwd=os.getcwd()
ls=os.listdir(cwd)
r=[]
tau=[]
tauerror=[]
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
		

		inf=2
		up=5
		aj=ajuste(x,y,inf,up)
		tau.append(-aj[0])
		tauerror.append(aj[5])
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
plt.plot([inf,up],[-tau[i]*inf+ordenada[i],-tau[i]*up+ordenada[i]],'r',label=r"$\tau$ = {e} $\pm$ {e1} ""\n $p_c(L = {h})$ = {j} \n $R^2$ = {k}".format(e=tau[i], e1=tauerror[i], j=p[i],k=r[i],h=l))
plt.xlabel("ln(s)")
plt.ylabel("ln($n_s$)")
plt.title("Ajuste de la distribucion de fragmentos para L = " + str(l) +"\n(Obtencion de "r"$\tau$)")
plt.legend(loc='best')
plt.savefig("tau"+ str(l)+ ".png")
plt.show()





