import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 11 - Regression\1. Simple Linear Regression\DataSet\canada_per_capita_income.csv" )
print( f"data :- \n{ data }\n" )

#Dividing the Data into x and y
x = data.loc[ :, 'year' ]
y = data.loc[ :, 'IncomePerCapita' ]

print( f"x.head() :- \n{ x.head() }\n" )
print( f"y.head() :- \n{ y.head() }\n" )

#Checking the nul value in x and y
print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print( f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )

#Checking the Datatypes of x and y
print( f"x.dtypes :- \n{ x.dtypes }\n" )
print( f"y.dtypes :- \n{ y.dtypes }\n" )

print( f"x.shape = { x.shape }" )
print( f"y.shape = { y.shape }" )

from sklearn.linear_model import LinearRegression
model=LinearRegression()

print( f"Before Data Frame x.shape = { x.shape }" )
x = pd.DataFrame( x )
print( f"After Data Frame x.shape = { x.shape }" )

#TIP :- before fitting/Training the data make sure that x is not one dimensional data.
# Otherwise it will give error
model.fit( x, y )       #x and y is training data

predicted_value = model.predict( x )    #x as test data

intercept = model.intercept_
coef = model.coef_

temp = data.copy()
temp['pred'] = predicted_value
print( temp )

print(f"Intercept = { intercept }\n")
print(f"Co-Efficient = { coef }")

print( f"model.predict( [[2019]] ) = { model.predict( [[2019]] ) }\n" )

#m = coef and c = intercept
print( f"( 2019*coef ) + intercept = { ( 2019*coef ) + intercept }\n" )

#Score,
#Syntax :- model.score( x_test, y-test )
print( f"model.score( x, y ) = { model.score( x, y ) * 100 } %" )               #To check the accuract of Predicted Value

import matplotlib.pyplot as plt

plt.plot( x, y, label = 'Actual', color = 'blue', marker = '+', linestyle = '' )
plt.plot( x, predicted_value , label = 'Prediction', color = 'red', marker = '*', linestyle = '' )
plt.legend()
plt.xlabel( 'X' )
plt.ylabel( 'Y V/s Y_Prediction' )
plt.title( 'Linear Regression' )
plt.show()

print( f"data.loc[ 45, 'year' ] = { list( data.loc[ 45, : 'IncomePerCapita' ] )[1] }" )
print( f"model.predict( [[2015]] ) = { list( model.predict( [[2015]] ) ) }" )

plt.plot( 2015, list( data.loc[ 45, : 'IncomePerCapita' ] )[1], label = 'Actual', marker = '*' )
plt.plot( 2015, model.predict( [[2015]] )          , label = 'red', marker = '+' )
plt.show()