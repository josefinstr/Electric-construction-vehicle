import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches

trans = 0.9
comp = 0.85
pow_elec = 0.9
tot_veh_E = 26.4# * 0.5
charge_time = 0.5*3 #hr
stor_charge_time = 24-1-charge_time
colors = ('red','blue','green','darkorange')
# print(colors[2])
fc = 0.6
ec = 0.8
grid2h = trans * pow_elec * ec * comp
h2elec = fc * pow_elec
runtime = np.arange(0,1,0.001)
storage_lst = []

# i = 1
# mw = i #MW
# grid_charge = mw * trans * pow_elec
# grid_energy = grid_charge * charge_time
# veh_E = tot_veh_E * runtime
# elec_from_storage = veh_E - grid_energy
# elec_from_storage = np.where((veh_E - grid_energy)<=0,0,veh_E - grid_energy)
# h_need_storage = elec_from_storage/h2elec
# max_stor = stor_charge_time * mw * grid2h
# h2_import = np.where((h_need_storage - max_stor)<=0,0,(h_need_storage - max_stor))
# h_stor_possible = np.where(h_need_storage>=max_stor,np.NaN,h_need_storage)
# plt.plot(runtime,h2_import,":",color=colors[i-1])
# # storage_lst.append(h_stor_possible)
# plt.plot(runtime,h_stor_possible,"-",color=colors[i-1])
# plt.grid()
# plt.xlim(0,0.5)

# plt.yticks()
# plt.ylim(0,10)
linewidth=2
plt.figure(figsize=(12,12))
plt.rc('font', size=15)
mw_lst = [0.5,1,2,3]
print(np.array(mw_lst)-1)
print(np.argmin(np.abs(np.array(mw_lst)-1)))
for i in mw_lst:
    mw = i #MW
    grid_charge = mw * trans * pow_elec
    grid_energy = grid_charge * charge_time
    veh_E = tot_veh_E * runtime
    elec_from_storage = veh_E - grid_energy
    elec_from_storage = np.where((veh_E - grid_energy)<=0,0,veh_E - grid_energy)
    h_need_storage = elec_from_storage/h2elec
    max_stor = stor_charge_time * mw * grid2h
    h2_import = np.where((h_need_storage - max_stor)<=0,0,(h_need_storage - max_stor))
    h_stor_possible = np.where(h_need_storage>=max_stor,max_stor,h_need_storage)
    # np.argmin(np.abs(np.array(mw_lst)-i))
    plt.plot(runtime,h2_import,"--",color=colors[np.argmin(np.abs(np.array(mw_lst)-i))],linewidth=linewidth)
    # storage_lst.append(h_stor_possible)
    plt.plot(runtime,h_stor_possible,"-",color=colors[np.argmin(np.abs(np.array(mw_lst)-i))],linewidth=linewidth)
# result = np.squeeze(storage_lst).T

plt.xticks(np.arange(0, 1+0.1, step=0.1))
plt.yticks(np.arange(0, 50+5, step=5))
plt.grid()
plt.ylim(0,45)
plt.xlim(0,1)


storage_cap = Line2D([0], [0], label='Storage Capacities', color='black', linestyle='-',linewidth=linewidth)
import_h2 = Line2D([0], [0], label='Imported Hydrogen', color='black', linestyle='--',linewidth=linewidth)

grid1 = mpatches.Patch(label='0.5 MW Grid', color='red')
grid2 = mpatches.Patch(label='1 MW Grid', color='blue')
grid3 = mpatches.Patch(label='2 MW Grid', color='green')
grid4 = mpatches.Patch(label='3 MW Grid', color='darkorange')
plt.legend(handles=[storage_cap,import_h2,grid1,grid2,grid3,grid4],ncol=2,loc='upper center')
plt.xlabel('Runtime fraction')
plt.ylabel('Energy Storage Capacities/Imported Hydrogen (MWh)')
plt.title('Hydrogen energy stroage capacities vs. runtime fraction')
plt.show()
# fc = 0.6
# ec = 0.8
# grid2h = trans * pow_elec * ec * comp
# h2elec = fc * pow_elec
# runtime = np.arange(0,1,0.001)
# storage_lst = []
# for i in [0.5,1,1.5,2]: #MW
#     mw = i
#     grid_charge = mw * trans * pow_elec
#     grid_energy = grid_charge * charge_time
#     veh_E = tot_veh_E * runtime
#     elec_from_storage = veh_E - grid_energy
#     elec_from_storage = np.where((veh_E - grid_energy)<=0,0,veh_E - grid_energy)
#     h_need_storage = elec_from_storage/h2elec
#     max_stor = stor_charge_time * mw * grid2h
    
#     h_stor_possible = np.where(h_need_storage>=max_stor,np.NaN,h_need_storage)
#     storage_lst.append(h_stor_possible)

# result = np.squeeze(storage_lst).T

# plt.plot(runtime,result,"--",color='black')
# plt.ylim(0)
# plt.show()