import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)

p=np.array([])
#ns=np.array([])
s=np.array([])
s=np.array(range(1,64**2+1))
pc=0.586663783913861
sigma=36.0/91.0

j=0
ns=np.empty((2079,len(s)))
#p=np.empty((2079,2079))

f = open("ns_p=0.586700,L=64.txt","r") 

nspc=np.array([])


aux=f.readline()
aux=aux.split(",")
aux=aux[1]
aux=aux.split(" ")

f.readline()
for line in f:

	aux=line.split(";")
	nspc=np.append(nspc,float(aux[1]))
	
#nspc=nspc/100000



for files in ls:
	
	if files.endswith(".txt"):

		f = open(files,"r") 
		
		
		#ns=np.array([])
		aux=f.readline()
		aux=aux.split(",")
		aux=aux[1]
		aux=aux.split(" ")
		p=np.append(p,float(aux[len(aux)-1]))


		f.readline()
		
		h=0
		for line in f:

			aux=line.split(";")
			ns[j][h]=float(aux[1])	
			h=h+1

		#ns[j][:]=ns[j][:]/100000

		"""if p[-1]==0.587500:
			nspc=ns"""


		auxo=0
		auxe=0
		s0=0
		auxo=np.nonzero(ns[j][:])
		auxe=np.where(ns[j][:]==(len(auxo)-1))
		s0=np.max(auxe[-1])
		
		#s0=len(s)

		lista=np.array([])

		for i in s:		
			if 0.0 < i/float(s0) and  i/float(s0) < 0.12:		
			
				lista=np.append(lista,int (i))	

		m=len(lista)	

		#print p
		#print len(p)
		#print ns
		#print lista[0]-lista[-1]
		print p[len(p)-1] 
		
		#lista=s
		"""
		ini=lista[0]
		fi=lista[0]+1

		fz=ns[j][ini:fi]/nspc[ini:fi]
		#lnfz=np.log(ns[ini:fi]) - np.log(nspc[ini:fi])

		z=(lista[0:1]**sigma)*(p[len(p)-1] -pc)/pc
		#z=lista[0:-1]
		#lnz=np.log(z)*sigma+np.log(p[-1]-pc)-np.log(pc)

		plt.plot(z,fz,'*r') 

		ini=lista[-1]
		fi=lista[-1]+1
		fz=ns[j][ini:fi]/nspc[ini:fi]
		z=(lista[-2:-1]**sigma)*(p[len(p)-1] -pc)/pc
		plt.plot(z,fz,'*k')									"""
		
		j=j+1


print lista[0]
print lista[-1]

ini=lista[0]+1
fi=lista[-1]
print (len (lista))

f1=np.zeros((lista[-1]+1,2079))
z=np.empty((lista[-1]+1,2079))

for j in range (2079):
	for o in range(int(lista[0]),int(lista[-1])+1):
		f1[o][j]=ns[j][o]/nspc[o]
		z[o][j]=(o**sigma)*(p[j] -pc)/pc


#fmax=np.zeros(lista[-1]+1)
#pmax=np.zeros(lista[-1]+1)
#zmax=np.zeros(lista[-1]+1)

fmax=np.array([])
pmax=np.array([])
zmax=np.array([])

for o in range(int(lista[0]),int(lista[-1])+1):
	plt.plot(z[o][:],f1[o][:],'.')

	maxi= np.max(f1[o][:])
	#print maxi
	fmax=np.append(fmax,maxi)

	auxi=np.where(f1[o][:]==np.max(f1[o][:]))
	auxe=np.max(auxi[-1])
	#print z[o][auxe]

	zmax=np.append(zmax,z[o][auxe])
	pmax=np.append(pmax,p[auxe])

	#plt.axvline(z[o][auxe], ymin=0, ymax = 3.5, linewidth=0.1, color='k')
	#plt.axhline(maxi, xmin=-2.5,xmax=2.5, linewidth=0.1, color='k')
	#plt.annotate(z[o][auxe], xy=(z[o][auxe], maxi), xytext=(z[o][auxi[-1]]+1.5,maxi), arrowprops=dict(facecolor='black', shrink=0.00002),)




plt.xlabel("z")
plt.ylabel("F(z)")
plt.show()		
ss=np.zeros(len(lista))
for i in range(len(lista)):
	ss[i]=int(lista[i])

np.savetxt("fz_L64.out", [fmax,zmax,ss,pmax], fmt="%1.6f", header = "fmax zmax s p")

"""
x=(s**sigma)*(pc-0.571400)/pc
plt.plot(x,nspc,'.-')
#plt.plot(np.log(x),np.log(nspc),'.-') 
"""

	
"""

#lnfz=np.log(ns)-np.log(nspc)

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
plt.xlabel("z")
plt.ylabel("F(z)")
plt.show()
"""

##np.savetxt("m2.out", [p,m2], fmt="%1.6f", header = "p m2")






