import pandas as pd

#hr_data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\Pre Processing\Topic 3 - MatPlotLib\DataSet\hrdata.csv" )

hr_data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\Pre Processing\Topic 3 - MatPlotLib\DataSet\hrdata.csv" )
print( f"hr_data.head() :- \n{ hr_data.head() }\n" )
print( f"hr_data.columns = { hr_data.columns }\n" )

import matplotlib.style as style
import matplotlib.pyplot as plt

print( f"Available Styles :- plt.style.available = { plt.style.available }\n" )

"""
style.use( 'classic' )
plt.hist( hr_data['Income'], bins = 10, color = 'red', alpha = 0.5, label="Without tight_layout()" )
plt.legend()
plt.show()

style.use( 'classic' )
plt.hist( hr_data['Income'], bins = 10, color = 'red', alpha = 0.5, label="With tight_layout()" )
plt.legend()
plt.show()
"""


"""
style.use( 'classic' )
plt.plot( hr_data['Income'], color = 'red', alpha = 0.5 )
plt.show()

style.use( 'classic' )
plt.pie( hr_data['Income'] )
plt.show()
"""

"""
count = 1
for i in plt.style.available:
    style.use( i )
    plt.plot( hr_data['Income'], color = 'red', alpha = 0.5, label = f"Current Style = { i }" )
    plt.title( f"Graph Number :- { count }" )
    plt.legend()
    plt.show()

    count = count + 1
"""