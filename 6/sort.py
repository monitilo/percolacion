import matplotlib.pyplot as plt
import sys
import numpy as np
import os


def swap(x,i,j):

	aux=x[i]
	x[i]=x[j]
	x[j]=aux

def sort(x,y):

	for i in range(0,len(x)):

		for j in range(0,len(x)):

			if(x[i]<x[j]):
		
				swap(x,i,j)
				swap(y,i,j)


p,m2=np.loadtxt("m2,L6.out")

sort(p,m2)

np.savetxt("m2,L6.txt", [p,m2], fmt="%1.6f", header = "p m2")

