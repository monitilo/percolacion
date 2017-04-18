import matplotlib.pyplot as plt
import sys

f = open(sys.argv[1],"r") 

f.readline()
f.readline()
p=[]
F=[]

for line in f:

	aux=line.split(";")
	p.append(float(aux[0]))
	F.append(float(aux[1])/27000)

plt.plot(p,F,'ro')
plt.plot([0,1],[0.5,0.5])
plt.ylabel("F")
plt.xlabel("p")
plt.show()
	
