import matplotlib.pyplot as plt
import sys
import numpy as np
import os
import scipy.stats as sp

cwd=os.getcwd()
ls=os.listdir(cwd)

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



for files in ls:

	if files.endswith(".txt"):

		
		l,p,m,sigma=np.loadtxt(files)
			
		x=np.log(l)
		y=np.log(m)
		
		ajus=sp.linregress(x,y)
		ajus=np.append(ajus,confint(x,y))
		plt.plot(x,y,'ro')
		plt.plot(x,x*ajus[0]+ajus[1],label='$D = {i} \pm {j}$'.format(i=ajus[0],j=ajus[5]))		
		plt.xlabel("ln(L)")
		plt.ylabel("ln(M)")
		plt.title("ln(M) vs ln(L)\n(Obtencion de la dimension fractal D)")
		plt.legend(loc='best')
		plt.savefig("dimfractal" + str(l[-1]) + ".png")
		plt.show()
		
		

		
		

