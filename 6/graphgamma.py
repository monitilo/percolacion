import matplotlib.pyplot as plt
import matplotlib.lines as lines
import sys
import numpy as np
import scipy.stats as sp
import os

cwd=os.getcwd()
ls=os.listdir(cwd)

p=np.array([])
m2=np.array([])
cmenos=m2
cmas=m2
r2mas=m2
r2menos=m2
deltap=m2

for files in ls:

	if files.endswith(".out"):
		
		f=open(files,"r")
		p,m2=np.loadtxt(files)

		imax=np.where(m2==np.max(m2))	
		imax=int(imax[0])+150
		pmax=p[imax]
		print pmax

		d=10  
		off=0

		for i in range(1,740/d+1):
			
			x = np.log(np.abs(p[imax+1+off:imax+i*d+1+off]-pmax))
			y = np.log(m2[imax+1+off:imax+i*d+1+off])
			aux=sp.linregress(x,y)
			cmas=np.append(cmas,aux[0])
			r2mas=np.append(r2mas,aux[2]**2)
			
			x = np.log(np.abs(p[imax-i*d-off:imax-off]-pmax))
			y = np.log(m2[imax-i*d-off:imax-off])
			aux=sp.linregress(x,y)
			cmenos=np.append(cmenos,aux[0])
			r2menos=np.append(r2menos,aux[2]**2)	

			deltap=np.append(deltap,np.abs(p[imax+i*d]-pmax))
				
		plt.figure()
		plt.plot(p,m2,'ro',p[imax],m2[imax],'go')
		lines.Line2D(np.array([p[imax],p[imax]]),np.array([0,m2[imax]]))
		plt.xlabel("p")
		plt.ylabel("$M_2$")
		plt.title("$M_2$ vs. p")
		plt.figure()
		plt.subplot(211)
		plt.plot(deltap,cmas,'ro-', label="$\gamma_+$")
		plt.plot(deltap,cmenos,'go-', label="$\gamma_-$")
		plt.legend()
		plt.title("$\gamma$")
		plt.subplot(212)
		plt.plot(deltap,r2mas,'ro-', label="$R^2+$")
		plt.plot(deltap,r2menos,'go-', label="$R^2-$")
		plt.legend()
		plt.title("$R^2$")
		plt.show()




	
	
