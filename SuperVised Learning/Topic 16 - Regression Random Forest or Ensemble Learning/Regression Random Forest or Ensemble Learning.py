import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 15 - Regression Random Forest or Ensemble Learning\Position_Salaries.csv" )

print( f"data.shape = { data.shape } and data.columns = { data.columns }" )
print()
print( data.head() )

x = data.loc[ :, ['Level'] ]
print( f"x.shape = {x.shape} and x.columns = { x.columns }" )
print()
y = data.loc[ :, ['Salary'] ]
print( f"y.shape = {y.shape} and y.columns = { y.columns }" )
print()

print( "x.isnull().sum()\n", x.isnull().sum() )
print()
print( "y.isnull().sum()\n", y.isnull().sum() )
print()
print( "x.dtypes\n", x.dtypes )
print()
print( "y.dtypes\n", y.dtypes )
print()

from sklearn.ensemble import RandomForestRegressor
rfr = RandomForestRegressor( n_estimators = 10 )
rfr.fit( x, y )

x = pd.DataFrame( x )
rfr.fit( x, y )
y_pred = rfr.predict( x )

print( y_pred )

print( rfr.score( x, y ) )

import matplotlib.pyplot as plt

plt.plot( x, y, label = 'Actual' )
plt.plot( x, y_pred, label = 'prediction' )
plt.legend()
plt.xlabel( 'X' )
plt.ylabel( 'Y V/s Y_pred' )
plt.title( 'Regression Random Forest or Ensemble Learning' )
plt.show()