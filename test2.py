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

runtime = 0.4
grid = 1

act_veh_usage_1c = runtime*tot_veh_E/3
grid_charge_pow = grid * trans * pow_elec
grid_charge_energy = charge_time * grid_charge_pow
elec_from_storage = np.where(act_veh_usage_1c > grid_charge_energy, act_veh_usage_1c - grid_charge_energy,0)

max_need_bat_1c = storage_charge_time*grid*grid2bat/bat_discharging
need_bat_1c = elec_from_storage/bat_discharging
need_bat_1c = np.where(need_bat_1c>max_need_bat_1c,max_need_bat_1c,need_bat_1c)

night_stor = 3*((elec_from_storage/bat_discharging)-max_need_bat_1c)
night_stor = np.where(night_stor>0,night_stor,0)
max_night_stor = stor_night_charge_time * grid * grid2bat
storage = need_bat_1c + night_stor
storage = np.where(night_stor > max_night_stor,need_bat_1c + max_night_stor,need_bat_1c + night_stor)
import_stor = night_stor - stor_night_charge_time*grid*grid2bat
import_stor = np.where(import_stor>0,import_stor,0)

