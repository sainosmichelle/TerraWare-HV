import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
name="VA01G"
#path=r"C:\Users\52551\Downloads\VA Inversion Geoexplorer"
path = r"C:\Users\52551\Downloads\Penoles"
#path = r"C:\Users\52551\Downloads\NOLTE\NOLTE\1.0 Huehuetoca\2.0 Proceso"
pathsave = os.path.join(path,name+'_VS.png')
#pathsave = os.path.join(path,name+'_VS.png')
path1 = os.path.join(path,'INV_G.txt')
inv= pd.read_csv(path1, skiprows=1, sep="\s+", header=None)
plt.figure(figsize=(3,8))
plt.plot(inv.iloc[:, 2], -inv.iloc[:, 0], 'k', linewidth=2)
plt.yscale("linear")
plt.xscale("linear")
plt.xlabel(r'Velocidad ($\frac{m}{s}$)')
plt.ylabel('Profundidad (m)')
#plt.xlim(np.min(inv.iloc[:, 4]) - 500, np.max(inv.iloc[:, 4]) + 500)
plt.xlim(0, np.max(inv.iloc[:, 2]) + 200)
plt.ylim(-np.max(inv.iloc[:, 0]), 0.0)
plt.title("VS "+name)
plt.grid( which='both')
#plt.axis('off')
plt.savefig(pathsave, transparent=True)
plt.show()

"""pathsave = os.path.join(path,name+'_VP.png')
plt.figure(figsize=(3,8))
plt.plot(inv.iloc[:, 1], -inv.iloc[:, 0], 'darkgreen')
plt.yscale("linear")
plt.xscale("linear")
plt.xlabel(r'Velocidad ($\frac{m}{s}$)')
plt.ylabel('Profundidad (m)')
plt.xlim(np.min(inv.iloc[:, 1]) - 300, np.max(inv.iloc[:, 1]) + 300)
plt.ylim(-np.max(inv.iloc[:, 0]), 0.0)
plt.title("VP Huehuetoca "+name)
plt.grid( which='both')
plt.savefig(pathsave, transparent=True)
plt.show()
"""