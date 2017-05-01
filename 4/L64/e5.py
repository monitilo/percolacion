import scipy.stats as sp
import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)
pc=0.586663783913861
sigma=36.0/91.0

for files in ls:

	if files.endswith(".out"):
		
		f=open(files,"r")
		fmax,zmax,s,p =np.loadtxt(files)

X=np.log(s)
Y=pc-p
plt.plot(X,Y,'.')

plt.xlabel("$ln(s)$")
plt.ylabel("$ln(p_c-p)$")
plt.show()		

inf=3
up=5

xfit=np.array([])
yfit=xfit
i=0

while(X[i] <= inf):
    i=i+1
while(X[i] <= up):
    xfit=np.append(xfit,X[i])
    yfit=np.append(yfit,Y[i])
    i=i+1

p=sp.linregress(xfit,yfit)
plt.plot(xfit,yfit,'go',xfit,xfit*p[0]+p[1],'r')

plt.annotate("ajuste $ \sigma ln(s); viene\ de\ p_{max} - p_c = s^\sigma$", xy=(3.5, 3.5*p[0]+p[1]), xytext=(3.5+0.3,3.5*p[0]+p[1]+0.01), arrowprops=dict(facecolor='black', shrink=0.00002),)

plt.xlabel("$ln(s)$")
plt.ylabel("$ln(p_c-p)$")
#plt.xlim(2.9, 5)
#plt.ylim(0.035, 0.13)
p[0], -sigma
