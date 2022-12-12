import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as mpatches

trans = 0.9 # transformer efficiency
comp = 0.85 # compressor efficiency
pow_elec = 0.9 # power controller electronics efficiency
tot_veh_E = 26.5732# (* 0.5) total vehicle energy demand

stor_night_charge_time = 12 #hr
colors = ('red','blue','green','darkorange')

bat_charging = 0.95 # battery charging efficiency
bat_discharging = 0.95 # battery discharging efficiency
roundtrip = 0.90 # battery roundtrip efficiency
grid2bat = trans * pow_elec * bat_charging # grid to battery efficiency
bat2veh = bat_discharging * pow_elec # battery to vehicle efficiency
bess_eff = grid2bat * bat2veh # BESS net efficiency

linewidth=2
plt.figure(figsize=(12,12))
plt.rc('font', size=15)


charge_time = 0.5 #hr
storage_charge_time = 3 #hr

mw_lst = np.array([1,2,3])
runtime_lst = np.arange(0,1,0.001)
storage_lst = []
import_stor_lst = []
night_stor_lst = []
for i in mw_lst:

    grid = i
    for j in runtime_lst:
        runtime = j
        act_veh_usage_1c = runtime*tot_veh_E/3
        grid_charge_pow = grid * trans * pow_elec
        grid_charge_energy = charge_time * grid_charge_pow
        elec_from_storage = np.where(act_veh_usage_1c > grid_charge_energy, act_veh_usage_1c - grid_charge_energy,0)
        
        max_need_bat_1c = storage_charge_time*grid*grid2bat
        need_bat_1c = elec_from_storage
        need_bat_1c = np.where(need_bat_1c>max_need_bat_1c,max_need_bat_1c,need_bat_1c)
        
        night_stor = 3*((elec_from_storage)-max_need_bat_1c)
        night_stor = np.where(night_stor>0,night_stor,0)
        max_night_stor = stor_night_charge_time * grid * grid2bat
        storage = need_bat_1c + night_stor
        storage = np.where(night_stor > max_night_stor,need_bat_1c + max_night_stor,need_bat_1c + night_stor)
        storage = storage/0.6
        import_stor = night_stor - stor_night_charge_time*grid*grid2bat
        import_stor = np.where(import_stor>0,import_stor,0)
        import_stor_lst.append(import_stor)
        storage_lst.append(storage)
        night_stor_lst.append(night_stor)
        
storage_arr = np.split(np.array(storage_lst), 3)
storage_arr = np.squeeze(storage_arr)
import_arr = np.split(np.array(import_stor_lst), 3)
import_arr = np.squeeze(import_arr)
# plt.plot(runtime_lst,import_stor,":",color=colors[np.argmin(np.abs((mw_lst)-i))],linewidth=linewidth)
plt.plot(runtime_lst,storage_arr[0],"-.",color='red',linewidth=linewidth)
plt.plot(runtime_lst,storage_arr[1],"-.",color='blue',linewidth=linewidth)
plt.plot(runtime_lst,storage_arr[2],"-.",color='green',linewidth=linewidth)
plt.plot(runtime_lst,import_arr[0],":",color='red',linewidth=linewidth)
plt.plot(runtime_lst,import_arr[1],":",color='blue',linewidth=linewidth)
plt.plot(runtime_lst,import_arr[2],":",color='green',linewidth=linewidth)

print(storage_arr[0,300]) # 1MW, runtime 0.3

mw_lst = np.array([1,2,3])
mw_lst = mw_lst + 0.499# from solar month 18
runtime_lst = np.arange(0,1,0.001)
storage_lst = []
import_stor_lst = []
night_stor_lst = []
for i in mw_lst:
    grid = i
    for j in runtime_lst:
        runtime = j
        act_veh_usage_1c = runtime*tot_veh_E/3
        grid_charge_pow = grid * trans * pow_elec
        grid_charge_energy = charge_time * grid_charge_pow
        elec_from_storage = np.where(act_veh_usage_1c > grid_charge_energy, act_veh_usage_1c - grid_charge_energy,0)
        
        max_need_bat_1c = storage_charge_time*grid*grid2bat
        need_bat_1c = elec_from_storage
        need_bat_1c = np.where(need_bat_1c>max_need_bat_1c,max_need_bat_1c,need_bat_1c)
        
        night_stor = 3*((elec_from_storage)-max_need_bat_1c)
        night_stor = np.where(night_stor>0,night_stor,0)
        max_night_stor = stor_night_charge_time * grid * grid2bat
        storage = need_bat_1c + night_stor
        storage = np.where(night_stor > max_night_stor,need_bat_1c + max_night_stor,need_bat_1c + night_stor)
        storage = storage/0.6
        import_stor = night_stor - stor_night_charge_time*grid*grid2bat
        import_stor = np.where(import_stor>0,import_stor,0)
        import_stor_lst.append(import_stor)
        storage_lst.append(storage)
        night_stor_lst.append(night_stor)

storage_arr = np.split(np.array(storage_lst), 3)
storage_arr = np.squeeze(storage_arr)
import_arr = np.split(np.array(import_stor_lst), 3)
import_arr = np.squeeze(import_arr)
plt.plot(runtime_lst,storage_arr[0],"-",color='red',linewidth=linewidth)
plt.plot(runtime_lst,storage_arr[1],"-",color='blue',linewidth=linewidth)
plt.plot(runtime_lst,storage_arr[2],"-",color='green',linewidth=linewidth)
plt.plot(runtime_lst,import_arr[0],"--",color='red',linewidth=linewidth)
plt.plot(runtime_lst,import_arr[1],"--",color='blue',linewidth=linewidth)
plt.plot(runtime_lst,import_arr[2],"--",color='green',linewidth=linewidth)

print(storage_arr[0,300]) # 1MW, runtime 0.3

plt.xticks(np.arange(0, 1+0.1, step=0.1))
plt.yticks(np.arange(0, 18+1, step=1))
plt.grid()
plt.ylim(4.950,18)
plt.xlim(0,1)
storage_cap_sol = Line2D([0], [0], label='Storage Capacities with solar power', color='black', linestyle='-',linewidth=linewidth)
storage_cap_nosol = Line2D([0], [0], label='Storage Capacities without solar power', color='black', linestyle='-.',linewidth=linewidth)
import_h2_sol = Line2D([0], [0], label='Imported battery with solar power', color='black', linestyle='--',linewidth=linewidth)
import_h2_nosol = Line2D([0], [0], label='Imported battery without solar power', color='black', linestyle=':',linewidth=linewidth)
grid1 = mpatches.Patch(label='1 MW Grid', color='red')
grid2 = mpatches.Patch(label='2 MW Grid', color='blue')
grid3 = mpatches.Patch(label='3 MW Grid', color='green')
plt.legend(handles=[storage_cap_sol,storage_cap_nosol,import_h2_sol,import_h2_nosol,grid1,grid2,grid3],ncol=1,loc='upper left')
plt.xlabel('Runtime fraction')
plt.ylabel('Energy storage capacity/Imported battery (MWh)')
plt.title('Battery swapping energy storage capacity vs. runtime fraction')
# plt.tight_layout()
plt.show()