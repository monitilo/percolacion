import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)

p=np.array([])
ns=np.array([])
s=np.array([])
m2=np.array([])
s=np.array(range(1,128**2+1))
s=s*s

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
		
		ns=ns/np.sum(ns)
		m2=np.append(m2,np.sum(ns*s))
		print p[len(p)-1]

np.savetxt("m2.out", [p,m2], fmt="%1.6f", header = "p m2")
		
		
