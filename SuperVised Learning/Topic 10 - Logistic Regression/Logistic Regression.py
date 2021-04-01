import  pandas as pd

############################Pre Processing##############
#Importing the Dataset
data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 10 - Logistic Regression\titanic_data.csv" )
print( data )
print()
print( f"data.columns = { data.columns }" )

#Divide the data into x and y
x = data.loc[ : , ['Pclass', 'Sex', 'Age', 'SibSp','Parch', 'Fare', 'Cabin', 'Embarked' ] ]
y = data.loc[ : , 'Survived' ]

print( f"x :- \n{ x }\n" )
print( f"y :- \n{ y }\n" )


#Null Values Checking
print(  f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print(  f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )

axes1 = x['Age'].plot( kind = 'hist', color = 'red' )
axes2 = x['Age'].plot( kind = 'density', secondary_y = True, ax = axes1, color = 'blue')
plt.title( 'sorted_mean - Density and Histogram Plot' )
axes1.set_ylabel( 'sorted_mean - Y Axis 1' )
axes2.set_ylabel( 'sorted_mean - Y Axis 2' )
axes1.set_xlabel( "sorted_mean - X Axis" )
plt.show()

x[ 'Age' ] = x[ 'Age' ].fillna( int( data['Age'].mean() ) )
print(  f"After Age, x.isnull().sum() :- \n{ x.isnull().sum() }\n" )

print( f"data['Age'].mean() = { data['Age'].mean() } and int( data['Age'].mean() ) = { int( data['Age'].mean() ) }" )

x = x.drop( ['Cabin'] , axis = 1 )
print(  f"After Cabin, x.isnull().sum() :- \n{ x.isnull().sum() }\n" )

print( f"data['Embarked'].unique() :- { data['Embarked'].value_counts() }\n" )
x['Embarked'] = x['Embarked'].fillna(  'S' )
print(  f"After Embarked, x.isnull().sum() :- \n{ x.isnull().sum() }\n" )

print( f"x['Embarked'].unique() = { x['Embarked'].unique() }")


#Data Type Checking
print( f"x.dtypes :- \n{ x.dtypes }\n" )
print( f"y.dtypes :- \n{ y.dtypes }\n" )

print( f"x.head() :- \n{ x.head() }\n" )

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

print( f"Before Le, x['Sex'].unique() = { x['Sex'].unique() }" )
x['Sex'] = le.fit_transform( x['Sex'] )
print( f"After Le, x['Sex'].unique() = { x['Sex'].unique() }" )

print( f"Before Le, x['Embarked'].unique() = { x['Embarked'].unique() }" )
x['Embarked'] = le.fit_transform( x['Embarked'] )
print( f"After Le, x['Embarked'].unique() = { x['Embarked'].unique() }" )

print( f"x.head() :- \n{ x.head() }\n" )

print( f"x.dtypes :- \n{ x.dtypes }\n x.shape = { x.shape }" )

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

for i in range( 0, 21 ):
    x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.1, random_state = i )
    lr = LogisticRegression()
    lr.fit( x_train, y_train )
    print( f"i = {i} and Score = { lr.score( x_test, y_test ) }" )
    

x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.1, random_state = 4 )
lr = LogisticRegression()
lr.fit( x_train, y_train )

print( f"lr.score( x_test, y_test ) = { lr.score( x_test, y_test ) }" )
y_pred = lr.predict( x_test )

print( f"x_test.shape = { x_test.shape }, y_test.shape = { y_test.shape } and y_pred.shape = { y_pred.shape }" )
print( f"y_pred :- \n{ y_pred }\n" )


from sklearn.metrics import accuracy_score
accuracy = accuracy_score( y_test, y_pred )
print( f"accuracy :- { accuracy }" )

from sklearn.metrics import confusion_matrix
cm = confusion_matrix( y_test, y_pred )
print( f"cm :- \n{ cm }\n" )

correct = cm[0][0] + cm[1][1]
incorrect = cm[0][1] + cm[1][0]

print( f"correct = { correct }, incorrect = { incorrect } and accuracy = { correct/ ( correct + incorrect ) }" )

import matplotlib.pyplot as plt

plt.plot( x_test, y_test, label = 'Existing', color = 'blue', marker = '+', linestyle = '' )
plt.plot( x_test, y_pred, label = 'Precition', color = 'red', marker = '*', linestyle = '' )
plt.legend()
plt.xlabel( "X_Test" )
plt.ylabel( "Y_Test V/s Y_pred" )
plt.title( "Logistic Regression" )
plt.show()