"""
 y = 0, 1, 2

svc -> 0 or 1 or 2

svr = -1 to 1

y -> classification columns
x -> Any type of col
"""

import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 17 - Support Vector Regression( SVR )\Social_Network_Ads.csv" )

print( f"data :- \n{ data }" )

x = data.loc[ :, ['Gender', 'Age', 'EstimatedSalary' ] ]
y = data.loc[ :, 'Purchased' ]

print( f"x :- \n{ x }\n" )
print( f"y :- \n{ y }\n" )

print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print( f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )

print( f"x.dtypes :- \n{ x.dtypes }\n" )
print( f"y.dtypes :- \n{ y.dtypes }\n" )

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

print( f"Before LE, x['Gender'].unique() :- { x['Gender'].unique() }\n" )
x['Gender'] = le.fit_transform( x['Gender'] )
print( f"After LE, x['Gender'].unique() :- { x['Gender'].unique() }\n" )

print( f"x :- \n{ x }\n" )

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.3 )

print( f"x_train = { x_train } \nand x_train.shape = { x_train.shape }" )
print( f"x_test = { x_test } \nand x_test.shape = { x_test.shape }" )
print( f"y_train = { y_train } \nand y_train.shape = { y_train.shape }" )
print( f"y_test = { y_test } \nand y_test.shape = { y_test.shape }" )

from sklearn.preprocessing import StandardScaler
ssc = StandardScaler()

print( f"type( x_train ), type( x_test ) = { type( x_train ), type( x_test ) }" )

x_train = ssc.fit_transform( x_train )
x_test = ssc.fit_transform( x_test )

print( f"After Standard Scaler, x_train :- \n{ x_train }\n" )
print( f"After Standard Scaler, x_test :- \n{ x_test }\n" )
print( f"type( x_train ), type( x_test ) = { type( x_train ), type( x_test ) }" )

from sklearn.svm import SVR, SVC
svr = SVR( kernel = 'rbf' )
svc = SVC( kernel = 'rbf' )

svr.fit( x_train, y_train )
svc.fit( x_train, y_train )

y_pred_svr = svr.predict( x_test )
y_pred_svc = svc.predict( x_test )

print( f"svr.score( x_test, y_test ) = { svr.score( x_test, y_test ) }" )
print( f"svc.score( x_test, y_test ) = { svc.score( x_test, y_test ) }" )

print( f"x_test.shape = { x_test.shape }, y_pred_svc.shape = { y_pred_svc.shape } and y_test.shape = { y_test.shape }" )
print( f"x_test.shape = { x_test.shape }, y_pred_svr.shape = { y_pred_svr.shape } and y_test.shape = { y_test.shape }" )

print( f"x_test :- \n{ x_test }" )
print( f"y = \n{ y }\n" )
print( f"y_pred_svc = \n{ y_pred_svc }\n" )
print( f"y_pred_svr = \n{ y_pred_svr }\n" )

import matplotlib.pyplot as plt
plt.plot( x_test, y_test, label = "Actual", color = 'blue', marker = '+', linestyle = '' )
plt.plot( x_test, y_pred_svc, label = "y_pred_svc Prediction", color = 'red', marker = '*', linestyle = '' )
plt.plot( x_test, y_pred_svr, label = "y_pred_svr Prediction", color = 'green', marker = '*', linestyle = '' )
plt.legend()
plt.show()