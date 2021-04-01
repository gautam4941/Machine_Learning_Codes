import pandas as pd

iris_data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 14 - Regression Decision Tree\iris.csv" )
position_data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 14 - Regression Decision Tree\Position_Salaries.csv" )

print( f"iris_data :- \n{ iris_data }\n" )
print( f"position_data :- \n{ position_data }\n" )

iris_x = iris_data.loc[ : , "sepal_length" : "petal_width" ]
iris_y = iris_data.loc[ : , "species" ]

position_x = position_data.loc[ :, ['Level'] ]
position_y = position_data.loc[ :, 'Salary' ]

print( f"position_x = { position_x }\n\n" )

print( "Checking Null Values of Iris Data Set, " )
print( f"iris_x.isnull().sum() :- \n{ iris_x.isnull().sum() }\n" )
print( f"iris_y.isnull().sum() :- \n{ iris_y.isnull().sum() }\n" )
print()
print( "Checking Null Values of Position Data Set, " )
print( f"position_x.isnull().sum() :- \n{ position_x.isnull().sum() }\n" )
print( f"position_y.isnull().sum() :- \n{ position_y.isnull().sum() }\n" )
print()

print( "Checking Data Type of Iris Data Set, " )
print( f"iris_x.dtypes :- \n{ iris_x.dtypes }\n" )
print( f"iris_y.dtypes :- \n{ iris_y.dtypes }\n" )
print()
print( "Checking Data Type of Position Data Set, " )
print( f"position_x.dtypes :- \n{ position_x.dtypes }\n" )
print( f"position_y.dtypes) :- \n{ position_y.dtypes }\n" )
print()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
iris_y = le.fit_transform( iris_y )

print( f"iris_y = { iris_y }\n\n" )

#Data Spliting
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( iris_x, iris_y, test_size = 0.2 )

print( f"x_train = { x_train }\n" )
print( f"y_train = { y_train }\n" )
print()
print( f"iris_x.shape = { iris_x.shape } and type( iris_x ) = { type( iris_x ) }" )
print( f"iris_y.shape = { iris_y.shape } and type( iris_y ) = { type( iris_y ) }" )
print( f"x_train.shape = { x_train.shape } and type( x_train ) = { type( x_train ) }" )
print( f"x_test.shape = { x_test.shape } and type( x_test ) = { type( x_test ) }" )
print( f"y_train.shape = { y_train.shape } and type( y_train ) = { type( y_train ) }" )
print( f"y_test.shape = { y_test.shape } and type( y_test ) = { type( y_test ) }" )
print( f"position_x.shape = { position_x.shape } and type( position_x ) = { type( position_x ) }" )
print( f"position_y.shape = { position_y.shape } and type( position_y ) = { type( position_y ) }" )

from sklearn.preprocessing import StandardScaler
ssc = StandardScaler()

x_train = ssc.fit_transform( x_train )
x_test = ssc.fit_transform( x_test )

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
iris_dtr = DecisionTreeRegressor()
position_dtr = DecisionTreeRegressor()
# lr = LogisticRegression()

iris_dtr.fit( x_train, y_train )            #fit( DataFrame, numpy_array )
# lr.fit( x_train, y_train )
position_dtr.fit( position_x, position_y )

# iris_pred = lr.predict( x_test )
iris_pred = iris_dtr.predict( x_test )
position_pred = position_dtr.predict( position_x )      #predict(DataFrame) -> numpy_array

print( f"iris_pred = { iris_pred } and type( iris_pred ) = { type( iris_pred ) }\n" )
print( f"position_pred = { position_pred } and type( position_pred ) = { type( position_pred ) }\n" )

# print( f"lr.score( x_test, y_test ) = { lr.score( x_test, y_test ) }" )
print( f"iris_dtr.score( x_test, y_test ) = { iris_dtr.score( x_test, y_test ) }" )
print( f"position_dtr.score( position_x, position_y ) = { position_dtr.score( position_x, position_y ) }" )

import numpy as np
x_grid = np.arange( min( position_x['Level'] ), max( position_x['Level'] ), 0.1 )
print( f"x_grid = { x_grid }\n" )

x_grid = pd.DataFrame( x_grid )
print( f"x_grid = { x_grid }\n" )

y_pred_grid = position_dtr.predict( x_grid )
print( f"y_pred_grid :- \n{ y_pred_grid }\n" )

import matplotlib.pyplot as plt
plt.plot( position_x, position_y, label = 'Actual', marker = 'o', color = 'blue' )
plt.plot( position_x, position_pred, label = 'Prediction', marker = '*', color = 'red' )
plt.plot( x_grid, y_pred_grid, label = 'Grid_prediction', marker = '+', color = 'green' )
plt.title( 'POSITION V/S SALARY' )
plt.xlabel( 'POSITION' )
plt.ylabel( 'SALARY' )
plt.legend()
plt.show()


import matplotlib.pyplot as plt
plt.plot( x_test, y_test, label = 'Actual', marker = 'o', color = 'blue', linestyle = '' )
plt.plot( x_test, iris_pred, label = 'Prediction', marker = '*', color = 'red', linestyle = '' )
plt.title( 'Flower Prediction' )
plt.xlabel( 'POSTION' )
plt.ylabel( 'Species - Label' )
plt.legend()
plt.show()