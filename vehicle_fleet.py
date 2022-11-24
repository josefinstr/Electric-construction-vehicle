# importing package
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
# create data
df = pd.DataFrame([['1', 2, 1, 0, 0, 0, 0, 0, 0], ['2', 2, 3, 0, 0, 0, 0, 0, 0],
                   ['3', 2, 3, 0, 0, 0, 0, 0, 0], ['4', 2, 0, 0, 0, 0, 0, 0, 0],
                   ['5', 2, 0, 2, 1, 0, 0, 0, 0], ['6', 2, 0, 6, 0, 2, 0, 0, 0],
                   ['7', 2, 0, 7, 0, 2, 0, 0, 0], ['8', 2, 0, 8, 0, 2, 1, 0, 0],
                   ['9', 2, 0, 7, 1, 2, 1, 0, 0], ['10', 2, 0, 7, 1, 2, 1, 0, 0],
                   ['11', 2, 0, 8, 1, 2, 1, 0, 0], ['12', 2, 0, 8, 1, 1, 1, 1, 0],
                   ['13', 2, 0, 9, 1, 1, 1, 2, 0], ['14', 2, 0, 8, 1, 1, 1, 2, 0],
                   ['15', 2, 0, 11, 1, 1, 1, 2, 0], ['16', 2, 0, 13, 2, 1, 2, 2, 0],
                   ['17', 2, 0, 15, 2, 2, 2, 2, 0], ['18', 2, 0, 13, 3, 2, 2, 2, 1],
                   ['19', 0, 0, 0, 0, 0, 0, 0, 0], ['20', 2, 0, 12, 2, 2, 1, 2, 1],
                   ['21', 2, 0, 13, 2, 2, 1, 2, 1], ['22', 2, 0, 10, 3, 2, 2, 2, 1],
                   ['23', 2, 0, 0, 0, 0, 0, 0, 0], ['24', 2, 0, 0, 0, 0, 0, 0, 0]],
                  columns=['Month', 'Private car', 'Forestry machine',
                           'Excavator (crawler)', 'Excavator (wheel)', 'Tractor',
                           'Wheel loader', 'Truck', 'Crawler tractor'])
# view data
print(df)
# print(df['Month'])
 
# plot data in stack manner of bar type
fig1 = plt.figure(figsize=(5.5, 3.5))
ax1 = fig1.add_subplot(111)
# ax1.plot(df.x)
df.plot(x='Month', kind='bar', stacked=True, title='Vehicle fleet',ax=ax1)
plt.savefig("vehicle_fleet.png")
fig1.show()

# battery equivalent size vs. motor power
beq = np.array([85, 85, 85, 85, 114, 114, 260, 284, 427, 447, 1016, 813, 1016, 1016,
                1341, 1300, 1162, 1918, 1918, 2357, 1414, 2520, 2764, 2764, 2764,
                2764, 3251, 5141])
mpower = np.array([12, 12, 12, 12, 15.6, 15.6, 18.5, 31.2, 44.3, 43, 90.0, 90,
                   110.0, 110, 115, 129.0, 129, 168, 189, 220, 180, 226, 278,
                   278, 340, 340, 385, 449])

# solve for a and b
def best_fit(mpower, beq):

    xbar = sum(mpower)/len(mpower)
    ybar = sum(beq)/len(beq)
    n = len(mpower) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(mpower, beq)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in mpower]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

# solution
a, b = best_fit(mpower, beq)
#best fit line: y = 4.55 + 6.90x

#plot
fig2 = plt.figure(figsize=(5.5, 3.5))
ax2 = fig2.add_subplot(111)
ax2.scatter(mpower,beq,label='Data')
yfit = [a + b * xi for xi in mpower]
ax2.plot(mpower, yfit, 'r--',label="Fitted line: y = 6.15 + 9.66x")
ax2.set_title('Battery equivalent size vs. engine power', fontsize=15)
ax2.set_xlabel('Engine power [kW]', fontsize=13)
ax2.set_ylabel('Battery equivalent size [kWh]', fontsize=13)
ax2.legend()
ax2.grid()
fig2.savefig("b_eq_size.png")
fig2.show()

# energy demand
daily_demand = np.array([449	,746, 746, 300,	814,	1396, 1544, 2001, 2070,	2070,
                         2219, 2966, 3965, 3816, 4262, 5085, 5484, 5807, 0,
                         5133, 5282, 5362, 300, 300])
monthly_demand = np.array([8972.094612, 14916.28384, 14916.28384, 6000,
                           16285.31313, 27915.56912, 30887.66373, 40029.70521,
                           41398.7345, 41398.7345, 44370.82912, 59329.32839,
                           79301.42301, 76329.32839, 85245.61223, 101700.8722,
                           109686.5622, 116147.9474,	0, 102664.782, 105636.8767,
                           107231.6636, 6000, 6000])
per_charge = np.array([2990.698204, 4972.094612, 4972.094612, 2000, 5428.43771,
                       9305.189707, 10295.88791, 13343.23507, 13799.57817, 13799.57817,
                       14790.27637, 19776.4428, 26433.80767, 25443.10946, 28415.20408, 
                       33900.29074, 36562.18739, 38715.98248, 0, 34221.59401, 35212.29222,
                       35743.88786, 2000, 2000])
month_no = np.arange(1,25)
width = 0.25

#plot
# plt.figure(figsize=(20,13))
# plt.rc('axes', labelsize=50)
# plt.rc('xtick', labelsize=20)
fig3 = plt.figure(figsize=(12, 7))
ax3 = fig3.add_subplot(111)
ax3.bar(month_no, daily_demand, color = 'b',
        width = width, edgecolor = 'black',
        label='Daily energy demand [kWh/day]')
ax3.bar(month_no + width, monthly_demand, color = 'r',
        width = width, edgecolor = 'black',
        label='Monthly energy demand [kWh/month]')
ax3.bar(month_no + width*2, per_charge, color = 'g',
        width = width, edgecolor = 'black',
        label='Energy demand per charge [kWh/month]')
ax3.set_xticks(month_no)
ax3.tick_params(axis='x', labelsize=15)
ax3.tick_params(axis='y', labelsize=15)
ax3.set_xlabel("Month", fontsize=20)
ax3.set_ylabel("Energy demand [kWh]", fontsize=20)
ax3.set_title("Total vehicle energy demand", fontsize=20)
ax3.legend()
ax3.grid()
fig3.show()