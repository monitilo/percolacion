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
	plt.plot(xfit,yfit,'go')
	plt.plot(xfit,xfit*p[0]+p[1],label=r"$\beta$ = {h} $\pm$ {u}""\n $R^2$ = {z}".format(h=p[0],z=p[2]**2,u=p[5]))
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

		
		j=0
		pc=0.5730

		while p[j] <= pc:
			j = j + 1


		for i in range(j,len(pinf)):

			if pinf[i]!=0:

				y=np.append(y,np.log(pinf[i]))
				x=np.append(x,np.log(np.abs(p[i]-pc)))
				
		plt.figure(1)
		plt.plot(p,pinf,'ro')
		plt.figure(2)
		plt.plot(x,y,'ro')
		inf=-10
		up=-6
		aj=ajuste(x,y,inf,up)
		plt.xlabel("ln(p-$p_c$) ($p_c =" + str(pc) + ")$")
		plt.ylabel("ln($P_\infty$)")
		plt.legend(loc='upper left')
		plt.title("Ajuste $P_\infty$")
		plt.show()
		





