import pandas as pd

#Data Input
data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 11 - Regression\2. Multiple Regression\DataSet\Social_Network_Ads.csv" )

print( f"data :- \n{ data }\n" )
print( f"data.columns :- { data.columns }\n" )

#Pre Processing
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

print( f"x['Gender'].unique() = { x['Gender'].unique() }\n" )
# print( f"le.fit_transform( x['Gender'] ) :- \n{ le.fit_transform( x['Gender'] ) }\n" )

x['Gender'] = le.fit_transform( x['Gender'] )
print( f"x['Gender'].unique() = { x['Gender'].unique() }\n" )

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2 )

print( f"x_train :- \n{ x_train }\n" )
print( f"y_train :- \n{ y_train }\n" )
print( f"x_test :- \n{ x_test }\n" )
print( f"y_test :- \n{ y_test }\n" )

#Algorithm
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit( x_train, y_train )

#Prediction
y_pred = lr.predict( x_test )

for i in range( len( y_pred ) ):
   if( y_pred[i] > 0.5 ):
       y_pred[i] = 1
   else:
       y_pred[i] = 0

#Accuracy Checking
print( f"lr.score( x_test, y_test ) = { lr.score( x_test, y_test ) }" )

temp = x_test.copy()
temp['Actual_Y'] = y_test
temp['Predicted_Y'] = y_pred

print( f"temp :- \n{ temp }\n" )

#Visualization/ Plotting the Graph
import matplotlib.pyplot as plt
plt.plot( x_test['Age'], y_test, label = 'Actual', marker = '+', color = 'blue', linestyle = '' )
plt.plot( x_test['Age'], y_pred, label = 'Prediction', marker = '*', color = 'red', linestyle = '' )
plt.legend()
plt.show()