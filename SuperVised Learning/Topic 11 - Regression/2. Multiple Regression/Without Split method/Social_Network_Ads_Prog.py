import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 11 - Regression\2. Multiple Regression\DataSet\Social_Network_Ads.csv" )

print( f"data.head() :- \n{ data.head() }\n" )
print( f"data.columns :- { data.columns }\n" )

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

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit( x, y )

y_pred = lr.predict( x )

lr.score( x, y )

temp = x.copy()
temp['Actual_Y'] = y
temp['Predicted_Y'] = y_pred

import matplotlib.pyplot as plt
plt.plot( x['Gender'], y, label = 'Actual', marker = '+', color = 'blue', linestyle = '' )
plt.plot( x['Gender'], y_pred, label = 'Prediction', marker = '*', color = 'red', linestyle = '' )
plt.legend()
plt.show()