import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Kernal_SVM\Social_Network_Ads.csv" )
print( f"data :- \n{ data }\n" )

x = data.loc[ :, 'Gender' : 'EstimatedSalary' ]
y = data.loc[ :, 'Purchased' ]

print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print( f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )

print( f"x.dtypes :- \n{ x.dtypes }\n" )
print( f"y.dtypes :- \n{ y.dtypes }\n" )

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

x['Gender'] = le.fit_transform( x['Gender'] )
print( f"x.dtypes :- \n{ x.dtypes }\n" )

from sklearn.preprocessing import StandardScaler
ssc = StandardScaler()
x = ssc.fit_transform( x )

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2 )

#import matplotlib.pyplot as plt
#plt.plot( x['Gender'], x['Age'], marker = '+', linestyle = '', label = 'Gender and Age' )
#plt.plot( x['Age'], x['EstimatedSalary'], marker = '*', linestyle = '', label = 'Age and EstimatedSalary' )
#plt.plot( x['Gender'], x['EstimatedSalary'], marker = 'o', linestyle = '', label = 'Gender and EstimatedSalary' )
#plt.legend()
#plt.show()

from sklearn.svm import SVC
svc = SVC( kernel='rbf' )

svc.fit( x_train, y_train )
y_pred = svc.predict( x_test )

from sklearn.metrics import confusion_matrix
cm = confusion_matrix( y_test, y_pred )

print( f"cm :- \n{ cm }\n" )

accuracy = cm[0][0] + cm[1][1]
inaccurate = len( y_test ) - accuracy

print( f"Accuracy = { accuracy } and Accuracy % = { ( accuracy/len( y_test ) ) * 100 }" )
print( f"Inaccuracy = { inaccurate } and Inaccuracy % = { ( inaccurate/len( y_test ) ) * 100 }" )

import matplotlib.pyplot as plt
plt.plot( x_test, y_test, color = 'blue', marker = '+', linestyle = '', label = 'Actual' )
plt.plot( x_test, y_pred, color = 'red', marker = '*', linestyle = '', label = 'Prediction' )
plt.legend()
plt.xlabel( 'X_TEST' )
plt.ylabel( 'y_TEST V/s Y_PRED' )
plt.title( "KERNAL SVM" )
plt.show()