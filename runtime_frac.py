import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches

linewidth=3

# 1MW
frac_bat = np.array([0.491259,0.234319])
bat = np.array([10.3880,0.0000])
frac_H20_07 = np.array([0.31374,0.22384])
h2_07 = np.array([7.229,0.000])
frac_H20_08 = np.array([0.3471,0.2238])
h2_08 = np.array([8.262,0])

plt.rc('font', size=14) #controls default text size
plt.figure(figsize=(12,12))
plt.title("Stationary energy storage vs. runtime fraction")
plt.plot(frac_bat,bat,"r-",linewidth=linewidth)
plt.plot(frac_H20_07,h2_07,"r--",linewidth=linewidth)
plt.plot(frac_H20_08,h2_08,"r:",linewidth=linewidth)

# 1.1 MW
bat1_1mw = np.array([0,11.427075])
frac_bat1_1mw = np.array([0.2578,0.5404])
plt.plot(frac_bat1_1mw,bat1_1mw,"b-",linewidth=linewidth)

h_07_1_1mw = np.array([0,7.952])
frac_h_07_1_1mw = np.array([0.246221434122611,0.345110117602105])
plt.plot(frac_h_07_1_1mw,h_07_1_1mw,"b--",linewidth=linewidth)

h_08_1_1mw = np.array([0,9.0882])
frac_h_08_1_1mw = np.array([0.246221434122611,0.381840200037345])
plt.plot(frac_h_08_1_1mw,h_08_1_1mw,"b:",linewidth=linewidth)

# 2 MW
bat2mw = np.array([0,20.7765])
frac_bat2mw = np.array([0.4686,0.9825])
plt.plot(frac_bat2mw,bat2mw,"g-",linewidth=linewidth)

h_07_2mw = np.array([0,14.459])
frac_h_07_2mw = np.array([0.4477,0.627])
plt.plot(frac_h_07_2mw,h_07_2mw,"g--",linewidth=linewidth)

h_08_2mw = np.array([0,16.524])
frac_h_08_2mw = np.array([0.447675,0.69425])
plt.plot(frac_h_08_2mw,h_08_2mw,"g:",linewidth=linewidth)

plt.ylim(0,22)
plt.xlim(0.2,1)
plt.xlabel("Runtime fraction")
plt.ylabel("Storage Capacities (MWh)")

bat_leg = Line2D([0], [0], label='Battery', color='black', linestyle='-',linewidth=linewidth)
h07_leg = Line2D([0], [0], label='Hydrogen, $\eta_{EC}$=0.7, $\eta_{FC}$=0.5', color='black', linestyle='--',linewidth=linewidth)
h08_leg = Line2D([0], [0], label='Hydrogen, $\eta_{EC}$=0.8, $\eta_{FC}$=0.6', color='black', linestyle=':',linewidth=linewidth)
grid1 = mpatches.Patch(label='1 MW Grid', color='red')
grid2 = mpatches.Patch(label='1.1 MW Grid', color='blue')
grid3 = mpatches.Patch(label='2 MW Grid', color='green')

plt.legend(handles=[bat_leg,h07_leg,h08_leg,grid1,grid2,grid3],ncol=2,loc='upper center')

plt.grid()
plt.show()