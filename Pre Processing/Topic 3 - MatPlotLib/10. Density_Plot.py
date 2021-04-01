import pandas as pd

hr_data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\Pre Processing\Topic 3 - MatPlotLib\DataSet\hrdata.csv" )
print( f"data :- \n{ data }\n" )

import matplotlib.pyplot as plt

"""
hr_data['Income'].plot( kind='density' )
plt.xlabel('Income')
plt.title( 'Dnsity Plot for Income' )
plt.show()
"""

"""
hr_data['Income'].plot( kind='density', ls = '--' )
plt.xlabel('Income')
plt.title( '1. Density Plot for Income' )
plt.show()
"""

"""
#Plotting Histogram and Density Graph Together
axes1 = hr_data['Income'].plot( kind = 'hist', color = 'red' )
axes2 = hr_data['Income'].plot( kind = 'density', color = 'blue')
plt.title( '1. Density and Histogram Plot' )
plt.show()
"""

"""
axes1 = hr_data['Income'].plot( kind = 'hist', color = 'red' )
axes2 = hr_data['Income'].plot( kind = 'density', secondary_y = True, color = 'blue')
plt.title( '2. Density and Histogram Plot' )
plt.show()
"""

"""
axes1 = hr_data['Income'].plot( kind = 'hist', color = 'red' )
axes2 = hr_data['Income'].plot( kind = 'density', secondary_y = True, ax = axes1, color = 'blue')
plt.title( '3. Density and Histogram Plot' )
plt.show()
"""

"""
axes1 = hr_data['Income'].plot( kind = 'hist', color = 'red' )
axes2 = hr_data['Income'].plot( kind = 'density', secondary_y = True, ax = axes1, color = 'blue')
plt.title( '4. Density and Histogram Plot' )
axes1.set_ylabel( 'No of Employee' )
plt.show()

axes1 = hr_data['Income'].plot( kind = 'hist', color = 'red' )
axes2 = hr_data['Income'].plot( kind = 'density', secondary_y = True, ax = axes1, color = 'blue')
plt.title( '4. Density and Histogram Plot' )
axes1.set_ylabel( 'No of Employee' )
axes2.set_ylabel( 'Employee Density' )
plt.show()
"""

"""
axes1 = hr_data['Income'].plot( kind = 'hist', color = 'red' )
axes2 = hr_data['Income'].plot( kind = 'density', secondary_y = True, ax = axes1, color = 'blue')
plt.title( '4. Density and Histogram Plot' )
axes1.set_ylabel( 'No of Employee' )
axes2.set_ylabel( 'Employee Density' )
axes1.set_xlabel( "Axes 1- Income" )
plt.show()
"""