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
runtime = np.arange(0,1,0.001)

for i in mw_lst:
    ###########
    grid = i
    act_veh_usage_1c = runtime*tot_veh_E/3
    grid_charge_pow = grid * trans * pow_elec
    grid_charge_energy = charge_time * grid_charge_pow
    elec_from_storage = np.where(act_veh_usage_1c - grid_charge_energy > 0, act_veh_usage_1c - grid_charge_energy,0)
    
    # battery
    need_bat_1c = elec_from_storage/bat_discharging
    max_bat_stor = grid * storage_charge_time * grid2bat
    extra_bat_night = np.where(need_bat_1c > max_bat_stor,need_bat_1c-max_bat_stor,0)
    extra_bat_need_3c = extra_bat_night*3
    bat_prod_night = stor_night_charge_time * grid * grid2bat
    import_bat = (need_bat_1c*3)-(max_bat_stor+bat_prod_night)
    tot_bat_stor_size = np.where(bat_prod_night+max_bat_stor<need_bat_1c*3,bat_prod_night+max_bat_stor,need_bat_1c*3)
    tot_bat_stor_size = tot_bat_stor_size/0.6
    plt.plot(runtime,import_bat,":",color=colors[np.argmin(np.abs((mw_lst)-i))],linewidth=linewidth)
    plt.plot(runtime,tot_bat_stor_size,"-.",color=colors[np.argmin(np.abs((mw_lst)-i))],linewidth=linewidth)

mw_lst = np.array([1,2,3])
mw_lst = mw_lst + 0.499 # from solar month 18

for i in mw_lst:
    grid = i
    act_veh_usage_1c = runtime*tot_veh_E/3
    grid_charge_pow = grid * trans * pow_elec
    grid_charge_energy = charge_time * grid_charge_pow
    elec_from_storage = np.where(act_veh_usage_1c - grid_charge_energy > 0, act_veh_usage_1c - grid_charge_energy,0)
    
    # battery
    need_bat_1c = elec_from_storage/bat_discharging
    max_bat_stor = grid * storage_charge_time * grid2bat
    extra_bat_night = np.where(need_bat_1c > max_bat_stor,need_bat_1c-max_bat_stor,0)
    extra_bat_need_3c = extra_bat_night*3
    bat_prod_night = stor_night_charge_time * grid * grid2bat
    import_bat = (need_bat_1c*3)-(max_bat_stor+bat_prod_night)
    tot_bat_stor_size = np.where(bat_prod_night+max_bat_stor<need_bat_1c*3,bat_prod_night+max_bat_stor,need_bat_1c*3)
    tot_bat_stor_size = tot_bat_stor_size/0.6
    plt.plot(runtime,import_bat,"--",color=colors[np.argmin(np.abs(np.array(mw_lst)-i))],linewidth=linewidth)
    plt.plot(runtime,tot_bat_stor_size,"-",color=colors[np.argmin(np.abs(np.array(mw_lst)-i))],linewidth=linewidth)

plt.xticks(np.arange(0, 1+0.1, step=0.1))
plt.yticks(np.arange(0, 50+5, step=1))
plt.grid()
plt.ylim(0,45)
plt.xlim(0,1)
storage_cap_sol = Line2D([0], [0], label='Storage Capacities with solar power', color='black', linestyle='-',linewidth=linewidth)
storage_cap_nosol = Line2D([0], [0], label='Storage Capacities without solar power', color='black', linestyle='-.',linewidth=linewidth)
import_h2_sol = Line2D([0], [0], label='Imported battery/electricity with solar power', color='black', linestyle='--',linewidth=linewidth)
import_h2_nosol = Line2D([0], [0], label='Imported battery/electricity without solar power', color='black', linestyle=':',linewidth=linewidth)
grid1 = mpatches.Patch(label='1 MW Grid', color='red')
grid2 = mpatches.Patch(label='2 MW Grid', color='blue')
grid3 = mpatches.Patch(label='3 MW Grid', color='green')
plt.legend(handles=[storage_cap_sol,storage_cap_nosol,import_h2_sol,import_h2_nosol,grid1,grid2,grid3],ncol=2,loc='upper left')
plt.xlabel('Runtime fraction')
plt.ylabel('Energy storage capacity/Imported Hydrogen (MWh)')
plt.title('Battery energy storage capacity vs. runtime fraction')

plt.show()