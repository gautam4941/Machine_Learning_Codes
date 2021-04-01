import pandas as pd
pd.set_option('display.max_columns', None)

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\Recursive Feature Elimination (RFE)\insurance.csv" )
print( data )


x = data.loc[ : , 'age' : 'region' ]
y = data.loc[ : , 'charges' ]

print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print( f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )

print( f"Before LE, x.dtypes :- \n{ x.dtypes }\n" )
print( f"Before LE, y.dtypes :- \n{ y.dtypes }\n" )

#Make own inbuilt Function to handle object dtypes
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

x['sex'] = le.fit_transform( x['sex'] )
x['smoker'] = le.fit_transform( x['smoker'] )
x['region'] = le.fit_transform( x['region'] )

print( f"After LE, x.dtypes :- \n{ x.dtypes }\n" )
print( f"After LE, y.dtypes :- \n{ y.dtypes }\n" )

import matplotlib.pyplot as plt

for i in x.columns:
    plt.boxplot( x[i] )
    plt.title( f"{i} Columns" )
    plt.show()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2, random_state = 0 )

from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

rfe_accuracy_list = []

def run_Linear_regression( x_train, y_train, x_test, y_test ):
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    return lr.score(x_test, y_test), lr

for i in range( 1, len( x_train.columns )+1 ):
    lr = LinearRegression()
    rfe = RFE( lr.fit( x_train, y_train ), n_features_to_select = i )
    rfe.fit(x_train, y_train)
    rfe_x_train = rfe.transform(x_train)
    rfe_x_test = rfe.transform(x_test)

    accuracy = run_Linear_regression(rfe_x_train, y_train, rfe_x_test, y_test)[0]
    print(f"Linear Regression with n_features_to_select = {i}, Accuracy :- ", accuracy )
    rfe_accuracy_list.append( accuracy )

print()
print( f"rfe_accuracy_list :- { rfe_accuracy_list }\n" )

lr = LinearRegression()
rfe = RFE( lr.fit( x_train, y_train ), n_features_to_select = 5 )
rfe.fit(x_train, y_train)
rfe_x_train = rfe.transform(x_train)
rfe_x_test = rfe.transform(x_test)

accuracy, new_lr = run_Linear_regression(rfe_x_train, y_train, rfe_x_test, y_test), lr
print(f"Linear Regression with n_features_to_select = 5, Accuracy :- {accuracy}\n" )

print( f"Coffecients = { new_lr.coef_ }" )
print( f"Intercept = { new_lr.intercept_ }\n" )

print( f"Total Columns :- { x_train.columns }\n" )
print( f"Columns Selected :- { x_train.columns[ rfe.get_support() ] }" )

y_pred = new_lr.predict( x_test )


plt.plot( x_test, y_test, color = 'blue', label = 'Actual', marker = '+', linestyle = '' )
plt.plot( x_test, y_pred, color = 'red', label = 'Predict', marker = '*', linestyle = '' )
plt.legend()
plt.xlabel( 'X_TEST' )
plt.ylabel( 'Y_TEST V/s Y_PRED' )
plt.title( 'RFE + LR' )
plt.show()


for i in x_train.columns[ rfe.get_support() ]:
    plt.plot( x_test[i], y_test, color = 'blue', label = 'Actual', marker = '+', linestyle = '' )
    plt.plot( x_test[i], y_pred, color = 'red', label = 'Predict', marker = '*', linestyle = '' )
    plt.legend()
    plt.xlabel( i )
    plt.ylabel( 'Y_TEST V/s Y_PRED' )
    plt.title( 'RFE + LR' )
    plt.show()
