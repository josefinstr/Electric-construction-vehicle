import numpy as np
import matplotlib.pyplot as plt

bat_size = np.array([0, 0, 0.42, 0.98, 1.61, 2.33, 3.17, 4.14, 5.29, 6.67, 10.23])
rratio_bat = np.array([4.8, 4.5, 4.25, 4.0, 3.75, 3.5, 3.25, 3.0, 2.75, 2.5, 2.03])

h2_size_eff1 = np.array([0, 0, 0.79, 1.85, 3.05, 4.43, 6.01, 6.41])
h2_size_eff2 =np.array([0, 0, 0.65, 1.54, 2.54, 3.68, 5.01, 5.34, 6.55, 7.33])
rratio_h2_eff1 = np.array([4.8, 4.5, 4.25, 4.0, 3.75, 3.5, 3.25, 3.19])
rratio_h2_eff2 = np.array([4.8, 4.5, 4.25, 4.0, 3.75, 3.5, 3.25, 3.19, 3.0, 2.89])

fig2 = plt.figure(num=2, figsize=(7,7))
ax = plt.subplot(111)
ax.plot(rratio_bat, bat_size, linestyle='--', marker='o', color='r', label='Battery storage')
ax.plot(rratio_h2_eff1, h2_size_eff1, linestyle='--', marker='o', color='b', label='Hydrogen storage, $η_{FC} = 0.5$, $η_{EC} = 0.7$')
ax.plot(rratio_h2_eff2, h2_size_eff2, linestyle='--', marker='o', color='g', label='Hydrogen storage, $η_{FC} = 0.6$, $η_{EC} = 0.8$')
plt.title("Stationary energy storage (MWh) vs. runtime ratio", fontweight='bold', fontsize=15)
plt.xlabel('Runtime ratio', fontsize=15)
plt.ylabel('Energy storage size (MWh)', fontsize=15)
ax.legend(fontsize=14)
plt.grid()
plt.savefig("storage_size.png")
plt.show()