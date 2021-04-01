import pandas as pd

data = pd.read_csv( r"hrdata.csv" )

print( f"data :- \n{ data }\n" )

import matplotlib.pyplot as plt

"""
plt.boxplot( data['Income'] )
plt.show()
"""

"""
iris_data = pd.read_csv( 'iris.csv' )
print( f"iris_data :- \n{ iris_data }\n" )

iris_data.plot( kind = 'box', color = 'red' )
plt.title( "Box Plot 1" )
plt.show()
"""