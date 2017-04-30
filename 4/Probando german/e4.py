import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)

p=np.array([])
ns=np.array([])
s=np.array([])
s=np.array(range(1,128**2+1))
pc=0.5874499606179948
sigma=36.0/91.0

f = open("ns_p=0.587500,L=128.txt","r") 

nspc=np.array([])


aux=f.readline()
aux=aux.split(",")
aux=aux[1]
aux=aux.split(" ")

f.readline()
for line in f:

	aux=line.split(";")
	nspc=np.append(nspc,float(aux[1]))
	
nspc=nspc/100000


for files in ls:
	
	if files.endswith(".txt"):

		f = open(files,"r") 
		
		ns=np.array([])
		aux=f.readline()
		aux=aux.split(",")
		aux=aux[1]
		aux=aux.split(" ")
		p=np.append(p,float(aux[len(aux)-1]))
		f.readline()
		


		for line in f:

			aux=line.split(";")
			ns=np.append(ns,float(aux[1]))
		
		ns=ns/100000

		"""if p[-1]==0.587500:
			nspc=ns"""


		auxo=0
		auxe=0
		s0=0
		auxo=np.nonzero(ns)
		auxe=np.where(ns==(len(auxo)-1))
		s0=np.max(auxe[-1])
		
		#s0=len(s)

		lista=np.array([])

		for i in s:		
			if 0.01 < i/float(s0) and  i/float(s0) < 0.12:		
			
				lista=np.append(lista,int (i))	

		m=len(lista)	

		#print p
		#print len(p)
		#print ns
		#print lista[0]-lista[-1]
		print p[len(p)-1] 
		
		#lista=s

		ini=lista[-1]
		fi=lista[-1]+1

		fz=ns[ini:fi]/nspc[ini:fi]
		lnfz=np.log(ns[ini:fi]) - np.log(nspc[ini:fi])

		z=(lista[-2:-1]**sigma)*(p[len(p)-1] -pc)/pc
		#z=lista[0:-1]
		lnz=np.log(z)*sigma+np.log(p[-1]-pc)-np.log(pc)

		plt.plot(z,fz,'.-')



plt.xlabel("z")
plt.ylabel("F(z)")
plt.show()			
		
"""
lnfz=np.log(ns)-np.log(nspc)

#eps=(p-pc)/pc

#epsmean=np.sum(eps)/len(eps)

#z=np.log(s)*sigma+ np.log(epsmean)

z=np.array([])
#z=np.array(range(1,len(s)+1))

x=np.linspace(1,1.5,len(s))

lnz=np.log(z)
lnx=np.log(x)

print(len(s))
print(len(ns))

plt.plot(lnz,lnfz,'o',lnx,lnfz,'r*')
plt.xlabel("ln (z)")
plt.ylabel("ln(F(z))")
plt.show()
"""

##np.savetxt("m2.out", [p,m2], fmt="%1.6f", header = "p m2")






