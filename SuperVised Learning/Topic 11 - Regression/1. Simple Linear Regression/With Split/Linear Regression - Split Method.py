import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 11 - Regression\1. Simple Linear Regression\DataSet\canada_per_capita_income.csv" )
print( f"data.head() :- \n{ data.head() }" )
print( f"data.shape = { data.shape }\n" )

x = data.loc[ :, 'year' ]
y = data.loc[ :, 'IncomePerCapita' ]

print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print( f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )

print( f"x.dtypes :- \n{ x.dtypes }\n" )
print( f"y.dtypes :- \n{ y.dtypes }\n" )


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2 )

print( f"x_train :- \n{ x_train }\n and x_train.shape = { x_train.shape }" )
print( f"y_train :- \n{ y_train }\n and y_train.shape = { y_train.shape }" )
print( f"x_test :- \n{ x_test }\n and x_test.shape = { x_test.shape }" )
print( f"y_test :- \n{ y_test }\n and y_test.shape = { y_test.shape }" )

x_train = pd.DataFrame( x_train )
x_test = pd.DataFrame( x_test )

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit( x_train, y_train )
y_pred = lr.predict( x_test )

print( f"lr.score( x_test, y_test ) = { lr.score( x_test, y_test ) }" )

temp = x_test.copy()
temp['Y'] = y_test
temp['PRED'] = y_pred

print( f"temp :- \n{ temp }\n" )

import matplotlib.pyplot as plt

plt.plot( temp['year'], temp['Y'], label = 'Actaul', marker = '+', color = 'blue', linestyle = '' )
plt.plot( temp['year'], temp['PRED'], label = 'Prediction', marker = '*', color = 'red' )
plt.legend()
plt.xlabel( 'X_TEST' )
plt.ylabel( 'Y_TEST V/s Y_PRED' )
plt.show()