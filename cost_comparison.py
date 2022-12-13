import matplotlib.pyplot as plt
import pandas as pd

#cost comparison

#SCENARIO 1
elec_1 = 21300000/(10^6) #MSEK electricity cost
cert_1 = 39755/(10^6) #MSEK certificate cost
vat_1 = 559064/(10^6) #MSEK value-added taxes
infr = 6834006/(10^6) #MSEK charging infrastructure cost

#SCENARIO 3
elec_2 = 18400000/(10^6) #MSEK electricity cost
cert_2 = 21035/(10^6) #MSEK certificate cost
vat_2 = 295814/(10^6) #MSEK value-added taxes
h2_stor_2 = 29400000/(10^6) #MSEK hydrogen storage cost
bat_stor_2 = 18200000/(10^6) #MSEK battery storage cost
bat_swapping = 21600000/(10^6) #MSEK battery swapping additional cost

#SCENARIO 3
elec_3 = 16500000/(10^6) #MSEK electricity cost
cert_3 = 33839/(10^6) #MSEK certificate cost
vat_3 = 374194/(10^6) #MSEK value-added taxes
h2_stor_3 = 29300000/(10^6) #MSEK hydrogen storage cost
bat_stor_3 = 15700000/(10^6) #MSEK battery storage cost
pv_park = 2100000/(10^6) #MSEK pv park cost

df = pd.DataFrame([['Scenario 1',elec_1,cert_1,vat_1,0,0,0,infr],['Scenario 2 Hydrogen',
                    elec_2,cert_2,vat_2,h2_stor_2,0,0,infr],['Scenario 2 Battery',elec_2,
                    cert_2,vat_2,0,bat_stor_2,0,infr],['Scenario 3 Hydrogen',elec_3,cert_3,
                    vat_3,h2_stor_3,0,pv_park,infr],['Scenario 3 Battery',elec_3,cert_3,
                    vat_3,0,bat_stor_3,pv_park,infr],['Battery swapping',elec_1,cert_1,vat_1,
                    0,bat_swapping,0,0]], columns=['Scenario', 'Electricity cost',
                    'Certificate cost', 'VAT', 'Hydrogen storage cost', 'Battery cost',
                    'Solar park', 'Charging infrastructure'])
                                                           
# view data
print(df)

# plot data in stack manner of bar type
fig1 = plt.figure(figsize=(30, 27))
ax1 = fig1.add_subplot(111)
# ax1.plot(df.x)
df.plot(x='Scenario', kind='bar', stacked=True,ax=ax1,fontsize=29)
plt.title('Cost comparison',fontsize=35)
plt.xlabel('Scenario',fontsize=33)
plt.ylabel('Cost [MSEK]',fontsize=33)
plt.legend(fontsize=32) #loc='upper right'
plt.grid()
plt.savefig("cost_comparison.png")
fig1.show()