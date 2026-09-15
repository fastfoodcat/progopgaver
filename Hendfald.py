import matplotlib.pyplot as plt
import numpy as np

N0 = 100
T_halv = 5
k = np.log(2) / T_halv

tid = np.arange(0, 51)
maengde = N0 * np.exp(-k * tid)

halverings_tid = np.arange(0, 51, T_halv)
halverings_maengde = N0 * np.exp(-k * halverings_tid)

plt.plot(tid, maengde)
plt.plot(halverings_tid, halverings_maengde, "ro")

plt.xlabel("Tid (år)")
plt.ylabel("Mængde (g)")
plt.grid(True)
plt.show()
