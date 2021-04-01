import pandas as pd

iris_data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 14 - Regression Decision Tree\iris.csv" )
print( f"iris_data :- \n{ iris_data }\n" )

iris_x = iris_data.loc[ : , "sepal_length" : "petal_width" ]
iris_y = iris_data.loc[ : , "species" ]

print( "Checking Null Values of Iris Data Set, " )
print( f"iris_x.isnull().sum() :- \n{ iris_x.isnull().sum() }\n" )
print( f"iris_y.isnull().sum() :- \n{ iris_y.isnull().sum() }\n" )
print()

print( "Checking Data Type of Iris Data Set, " )
print( f"iris_x.dtypes :- \n{ iris_x.dtypes }\n" )
print( f"iris_y.dtypes :- \n{ iris_y.dtypes }\n" )
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
print( f"y_test.shape = { y_test.shape } and type( y_test ) = { type( y_test ) }\n" )

from sklearn.preprocessing import StandardScaler
ssc = StandardScaler()

x_train = ssc.fit_transform( x_train )
x_test = ssc.fit_transform( x_test )

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
iris_dtr = DecisionTreeRegressor()
iris_dtr.fit( x_train, y_train )  #fit( DataFrame, numpy_array )

iris_data_for_prediction = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 13 - Regression Decision Tree\IRIS_PREDICTION.csv" )
print( f"iris_data_for_prediction :- \n{ iris_data_for_prediction }\n" )

x_for_prediction = iris_data_for_prediction.loc[ :, "sepal_length" : "petal_width" ]
# x_for_prediction = ssc.fit_transform( x_for_prediction )

print( f"x_for_prediction = \n{ x_for_prediction }\n" )

iris_pred = iris_dtr.predict( x_for_prediction )

print( f"iris_pred = { iris_pred } and type( iris_pred ) = { type( iris_pred ) }\n" )

print( f"iris_dtr.score( x_test, y_test ) = { iris_dtr.score( x_test, y_test ) }" )

import matplotlib.pyplot as plt

plt.plot( x_for_prediction, iris_pred, label = 'Prediction', marker = '*', color = 'red', linestyle = '' )
plt.title( 'Flower Prediction' )
plt.xlabel( 'POSTION' )
plt.ylabel( 'Species - Label' )
plt.legend()
plt.show()