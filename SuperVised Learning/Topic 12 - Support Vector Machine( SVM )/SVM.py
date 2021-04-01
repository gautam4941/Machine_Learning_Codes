import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 12 - Support Vector Machine( SVM )\Social_Network_Ads.csv" )
print( f"data :- \n{ data }" )

x = data.loc[ :, 'Gender' : 'EstimatedSalary' ]
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
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2 )

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

from sklearn.svm import SVC

svcob = SVC( kernel="rbf" )
svcob.fit( x_train, y_train )
#Predicting the test set results
y_pred = svcob.predict( x_test )

print( f"y_pred = { y_pred }\n" )

print( f"svcob.score( x_test, y_test ) = { svcob.score( x_test, y_test ) }" )

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

plt.plot( x_test, y_test, label = 'Actual', marker = '+', color = 'blue', linestyle = '' )
plt.plot( x_test, y_pred, label = 'Prediction', marker = '*', color = 'red', linestyle = '' )
plt.legend()
plt.xlabel( 'X_TEST' )
plt.ylabel( 'Y_TEST V/s Y_PRED' )
plt.title( "SVM when kernel is rbf" )
plt.show()

