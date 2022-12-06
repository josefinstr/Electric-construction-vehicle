import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches

linewidth=3

# 1MW
frac_bat = np.array([0,0.2604,0.5776])
bat = np.array([0,0,11.54])
frac_H20_07 = np.array([0.2487,0.3486])
h2_07 = np.array([0,7.229])
frac_H20_08 = np.array([0.2487,0.3857])
h2_08 = np.array([0,8.262])

plt.rc('font', size=14) #controls default text size
plt.figure(figsize=(9,9))
plt.title("Stationary energy storage vs. runtime fraction")
plt.plot(frac_bat,bat,"r-",linewidth=linewidth)
plt.plot(frac_H20_07,h2_07,"r--",linewidth=linewidth)
plt.plot(frac_H20_08,h2_08,"r:",linewidth=linewidth)

# 1.5 MW
bat1_5mw = np.array([0,0,17.3138])
frac_bat1_1mw = np.array([0,0.3905,0.8663])
plt.plot(frac_bat1_1mw,bat1_5mw,"b-",linewidth=linewidth)

h_07_1_5mw = np.array([0,10.844])
frac_h_07_1_5mw = np.array([0.3731,0.5229])
plt.plot(frac_h_07_1_5mw,h_07_1_5mw,"b--",linewidth=linewidth)

h_08_1_5mw = np.array([0,12.393])
frac_h_08_1_5mw = np.array([0.3731,0.5785])
plt.plot(frac_h_08_1_5mw,h_08_1_5mw,"b:",linewidth=linewidth)

# 2 MW
bat2mw = np.array([0,0,17.44])
frac_bat2mw = np.array([0,0.5207,1])
plt.plot(frac_bat2mw,bat2mw,"g-",linewidth=linewidth)

h_07_2mw = np.array([0,14.46])
frac_h_07_2mw = np.array([0.4974,0.6972])
plt.plot(frac_h_07_2mw,h_07_2mw,"g--",linewidth=linewidth)

h_08_2mw = np.array([0,16.524])
frac_h_08_2mw = np.array([0.4974,0.7714])
plt.plot(frac_h_08_2mw,h_08_2mw,"g:",linewidth=linewidth)

plt.ylim(0,22.5)
plt.xlim(0.2,1)
plt.xlabel("Runtime fraction")
plt.ylabel("Storage Capacities (MWh)")

bat_leg = Line2D([0], [0], label='Battery', color='black', linestyle='-',linewidth=linewidth)
h07_leg = Line2D([0], [0], label='Hydrogen, $\eta_{EC}$=0.7, $\eta_{FC}$=0.5', color='black', linestyle='--',linewidth=linewidth)
h08_leg = Line2D([0], [0], label='Hydrogen, $\eta_{EC}$=0.8, $\eta_{FC}$=0.6', color='black', linestyle=':',linewidth=linewidth)
grid1 = mpatches.Patch(label='1 MW Grid', color='red')
grid2 = mpatches.Patch(label='1.5 MW Grid', color='blue')
grid3 = mpatches.Patch(label='2 MW Grid', color='green')

plt.legend(handles=[bat_leg,h07_leg,h08_leg,grid1,grid2,grid3],ncol=2,loc='upper center')

plt.grid()
plt.show()