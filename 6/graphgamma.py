import matplotlib.pyplot as plt
import matplotlib.lines as lines
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

def smooth(y,n):

	s=np.zeros(len(y))
	for i in range(0,n):

		s[i]=y[i]
		s[len(y)-1-i]=y[len(y)-1-i]

	for i in range(n,len(y)-n):
		
		s[i]=sum(y[i-n:i+n+1])/n
		
	return s


cwd=os.getcwd()
ls=os.listdir(cwd)

p=np.array([])
m2=np.array([])
cmenos=m2
cmas=m2
cmenosinc=m2
cmasinc=m2
r2mas=m2
r2menos=m2
deltap=m2

for files in ls:

	if files.endswith(".out"):
		
		f=open(files,"r")
		p,m2=np.loadtxt(files)

		imax=np.where(m2==np.max(m2))	
		imax=int(imax[0])-100
		pmax=p[imax]
		print pmax

		d=10
		off=0

		for i in range(1,800/d+1):
			
			x = np.log(np.abs(p[imax+1+off:imax+i*d+1+off]-pmax))
			y = np.log(m2[imax+1+off:imax+i*d+1+off])
			aux=sp.linregress(x,y)
			cmas=np.append(cmas,aux[0])
			r2mas=np.append(r2mas,aux[2]**2)
			aux=confint(x,y)
			cmasinc=np.append(cmasinc,aux[0])
			
			x = np.log(np.abs(p[imax-i*d-off:imax-off]-pmax))
			y = np.log(m2[imax-i*d-off:imax-off])
			aux=sp.linregress(x,y)
			cmenos=np.append(cmenos,aux[0])
			r2menos=np.append(r2menos,aux[2]**2)	
			aux=confint(x,y)
			cmenosinc=np.append(cmenosinc,aux[0])
			
			deltap=np.append(deltap,np.abs(p[imax+i*d]-pmax))
		
		resta=np.abs(cmenos-cmas)
		menor=np.where(resta==np.min(resta))
		menor=int(menor[-1])		
		plt.figure()
		plt.plot(p,m2,'ro',p[imax],m2[imax],'go')
		lines.Line2D(np.array([p[imax],p[imax]]),np.array([0,m2[imax]]))
		plt.xlabel("p")
		plt.ylabel("$M_2$")
		plt.title("$M_2$ vs. p")
		plt.savefig("m2vsp,L128.png")
		plt.figure()
		plt.subplot(211)
		plt.plot(deltap,cmas,'ro-', label="$\gamma_+$ = {i} $\pm$ {j}".format(i=-float('%.3f'%cmas[menor]),j='%.3f'%cmasinc[menor]))
		plt.plot(deltap[menor],cmas[menor], 'mo')
		plt.plot(deltap,cmenos,'go-', label="$\gamma_-$ = {i} $\pm$ {j}".format(i=-float('%.3f'%cmenos[menor]),j='%.3f'%cmenosinc[menor]))
		plt.plot(deltap[menor],cmenos[menor], 'mo')
		plt.legend(loc='best')
		plt.xlabel("ln(p-$p_c$)")
		plt.ylabel("ln($M_2(p-p_c)$)")
		plt.subplot(212)
		plt.plot(deltap,r2mas,'ro-', label="$R^2+$ = {i}".format(i='%.3f'%r2mas[menor]))
		plt.plot(deltap[menor],r2mas[menor], 'mo')
		plt.plot(deltap,r2menos,'go-', label="$R^2-$ = {i}".format(i='%.3f'%r2menos[menor]))
		plt.plot(deltap[menor],r2menos[menor], 'mo')
		plt.legend(loc='best')
		plt.xlabel("ln(p-$p_c$)")
		plt.ylabel("$R^2$")
		plt.savefig("gammaL128.png")
		plt.show()




	
	
