import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)

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

p=np.array([])
m2=np.array([])

for files in ls:

	if files.endswith(".out"):
		
		f=open(files,"r")
		p,m2=np.loadtxt(files,dtype='float')

		imax=np.where(m2==np.max(m2))
		imax=int(imax[0])
		pmax=p[imax]
		

		imenor=imax-600
		imayor=imax+600
	
		cmas=np.log(np.diff(m2[(imax+1):(imayor+1)])/np.diff(p[(imax+1):(imayor+1)]))
		cmenos=np.log(np.diff(m2[imenor:imax])/np.diff(p[imenor:imax]))
		cmenos=np.flipud(cmenos)
		
		x=np.log(np.abs(np.array(p[imax:(imayor-1)])-pmax))
				
		plt.figure()
		plt.plot(p,m2,'ro',p[imax],m2[imax],'go')
		plt.figure()
		plt.plot(x,cmas,'ro',x,cmenos,'go')
		plt.show()




	
	
