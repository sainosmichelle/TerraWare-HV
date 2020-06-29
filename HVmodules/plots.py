import matplotlib.pyplot as plt
import pandas as pd
import os
name="Estación 4546"
#path = r"C:\Users\52551\Downloads\NOLTE\NOLTE\2.0 Tlajomulco"
path = r"C:\Users\52551\Downloads\Penoles"
pathsave = os.path.join(path,name+'.png')
#path1 = os.path.join(path,name+'.hv')
path2 = os.path.join(path,'4546_HV.txt')
#geopsy= pd.read_csv(path1, skiprows=7, sep="\s+", header=None)
terraware= pd.read_csv(path2, skiprows=1, sep="\s+", header=None)
plt.figure(figsize=(9,5))
#plt.plot(geopsy.iloc[:,0],geopsy.iloc[:,1], 'k', label="gp H/V", linewidth=2)
#plt.plot(terraware.iloc[:,0],terraware.iloc[:,4], label=r'TerraWareHV:$\sqrt{\frac{NS+EW}{2 VE}}$')
plt.plot(terraware.iloc[:,0],terraware.iloc[:,1], 'k', label="TW H/V", linewidth=2)
plt.plot(terraware.iloc[:,0],terraware.iloc[:,2], '--r', linewidth=1)
plt.plot(terraware.iloc[:,0],terraware.iloc[:,3], '--r', linewidth=1)
plt.xscale("log")
plt.xlim(0.1, 15)
plt.legend()
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.title(name)
plt.grid( which='both')
plt.savefig(pathsave, transparent=True)
plt.show()


"""import numpy as np
import matplotlib.colors as mcolors
import copy
dict =mcolors.CSS4_COLORS
#nombres = dict.keys()
#print(dict)



lista_colors = list(dicti.keys())
np.asarray(lista_colors)
np.random.shuffle(lista_colors)
np.random.shuffle(lista_colors)
print(lista_colors)"""