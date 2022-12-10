import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches
linewidth=2
plt.figure(figsize=(15,10))
plt.rc('font', size=15)

h_stor=np.array([0,	0,	0,	0,	0,	0.543,	0.941,	2.166,	2.254,	2.254,	2.652,	5.032,	7.93	,7.532,	8.262,	8.262,	8.262,	8.262,	0,	8.262,	8.262,	8.262,	0,	0,])
bat_stor = np.array([0.00,	0.00,	0.00,	0.00	,0.00,	0.51	,0.89,	2.05	,2.14,	2.14,	2.51,	4.77,	7.51,	7.14,	8.27,	10.26,	11.13,	11.85,	0.00,	10.23,	10.61,	10.72,	0.00,	0.00])
h_import = np.array([-8.26,	-8.26,	-8.26,	-8.26,	-8.26,	-7.72,	-7.32,	-6.10,	-6.01,	-6.01,	-5.61,	-3.23,	-0.33,	-0.73,	0.46	,2.57,	3.49	, 4.25,	-8.26,	2.54	,2.94,	3.06	,-8.26,	-8.26])
bat_import = np.array([-11.7,	-24.9,	-24.9,	-5.1,	-26.4,	-48.4,	-54.8,	-74.5,	-75.9,	-75.9,	-82.3,	-120.5,	-167.0,	-160.6,	-179.8,	-213.6,	-228.3,	-240.6,	-2.3,	-213.1,	-219.5,	-221.4,	-5.1,	-5.1])
bat_import = np.where(bat_import<0,0,bat_import)
h_import = np.where(h_import<0,0,h_import)
month = np.linspace(1, 24,num=24)

plt.bar(month-0.125,h_stor,width=0.25,label='Hydrogen storage capacities required $η_{EC}/η_{FC} = 0.8/0.6$')
plt.bar(month-0.125,h_import,width=0.25,label='Hydrogen imported')
plt.bar(month+0.125,bat_stor,width=0.25,label='Battery storage capacities required')
plt.bar(month+0.125,bat_import,width=0.25,label='Battery imported')

plt.xlim(1,24)
plt.xticks(np.arange(1, 25, step=1))

plt.xlabel('Month')
plt.ylabel('Energy storage capacity/imported energy (MWh)')
plt.title('Energy storage capacity vs. month, runtime fraction = 0.3, 1 MW grid')
plt.legend()
plt.yticks(np.arange(0, 13, step=1))
plt.ylim(0,12)
plt.grid(axis='y')
plt.show()