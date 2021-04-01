import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 11 - Regression\3. Polynomial Regression\DataSet\Position_Salaries.csv" )

print( f"data :- \n{ data }\n" )

x = data.loc[ :, ['Level'] ]
y = data.loc[ :, ['Salary'] ]

print( f"x :- \n{ x }\n" )
print( f"y :- \n{ y }\n" )

print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print( f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )

print( f"x.dtypes :- \n{ x.dtypes }\n" )
print( f"y.dtypes :- \n{ y.dtypes }\n" )

import matplotlib.pyplot as plt
plt.plot( x, y, marker = '*' )
plt.xlabel('Level')
plt.ylabel( 'Salary' )
plt.show()

x = pd.DataFrame( x )

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit( x, y )

lr_y_pred = lr.predict( x )
print( f"lr_y_pred :- \n{ lr_y_pred }\n" )

# plt.plot( x, y, marker = '*', label = 'y' )
# plt.plot( x, lr_y_pred, marker = '*', label = 'Y_Pred -> LR( Precition )' )
# plt.xlabel('Level')
# plt.ylabel( 'Salary' )
# plt.legend()
# plt.show()

from sklearn.preprocessing import PolynomialFeatures

acc = []
for i in range( 1, 11 ):
	pf = PolynomialFeatures( degree = i )
	transformed_x = pf.fit_transform( x )
	lr2 = LinearRegression()
	lr2.fit( transformed_x, y )
	score = lr2.score( transformed_x, y )
	print( f"i = {i} and Score = { score }" )
	acc.append( score )

###We will get our almost optimum accuracy when degree = 4

pf = PolynomialFeatures( degree = 4 )
pf.fit_transform( x )

print( f"After Polynomial Fit Transform, x :- \n{ x }" )

transformed_x = pf.fit_transform( x )

print( f"transformed_x :- \n{ transformed_x }\n" )

lr2 = LinearRegression()
lr2.fit( transformed_x, y )

lr2_y_pred = lr2.predict( transformed_x )

plt.plot( x, y, marker = '*', color = 'blue', label = 'y' )                      #Given Data
plt.plot( x, lr_y_pred, marker = '*', color = 'green', label = 'Linear Regression' )    #Simple Linear Regression
plt.plot( x, lr2_y_pred, marker = '*', color = 'red', label = 'Polynomial Regression' )     #Polynomial Regression
plt.xlabel('Level')
plt.ylabel( 'Salary' )
plt.legend()
plt.show()


print( f"y :- \n{ y }\n" )
print( f"lr_y_pred :- \n{ lr_y_pred }\n" )
print( f"lr2_y_pred :- \n{ lr2_y_pred }\n" )

##############################Steps in Polynomial Regression###############
#1st make the Polynomial regression Object
#change the X value by doing poly_obj.fit_transform( x )
#get the predicted answer of Poly..reg

###############For Finding the Accuracy
# Find the mean value first by doing the ( sum of actual y )/ ( len(y) ** 2 )
# find the difference of each y[i] and poly_y_pred[i]. if the diffrence value is less than or
# equals to mean then it correctn otherwise it is incorrect.

#Note :- While finding the diffrence, we are concern about actual difference value not the + or - sign