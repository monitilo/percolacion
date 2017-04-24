import matplotlib.pyplot as plt
import sys
import numpy as np
import os

cwd=os.getcwd()
ls=os.listdir(cwd)


for files in ls:

	if files.endswith(".out"):
		
		p,m2=np.loadtxt(files)

		plt.plot(p,m2,'ro')
		plt.show()
