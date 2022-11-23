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
 
# plot data in stack manner of bar type
df.plot(x='Month', kind='bar', stacked=True,
        title='Vehicle fleet')
plt.savefig("vehicle_fleet.png")
plt.show()

# battery equivalent size vs. motor power
beq = np.array([61, 61, 61, 61, 81, 81, 186, 203, 305, 319, 726, 581, 726, 726,
                958, 929, 830, 1370, 1370, 1684, 1010, 1800, 1974, 1974, 1974,
                1974, 2322, 3672])
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
plt.figure(num=None)
plt.scatter(mpower,beq,label='Data')
yfit = [a + b * xi for xi in mpower]
plt.plot(mpower, yfit, 'r--',label="Fitted line: y = 4.55 + 6.90x")
plt.title('Battery equivalent size vs. engine power', fontsize=15)
plt.xlabel('Engine power [kW]', fontsize=13)
plt.ylabel('Battery equivalent size [kWh]', fontsize=13)
plt.legend()
plt.grid()
plt.savefig("b_eq_size.png")
plt.show()