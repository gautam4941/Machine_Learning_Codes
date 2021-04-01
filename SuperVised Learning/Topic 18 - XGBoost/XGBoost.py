import pandas as pd

data = pd.read_csv(r'C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 18 - XGBoost\Churn_Modelling.csv')

print( data.head() )
print( f"\ndata.columns = { data.columns }" )

x = data.loc[ :, "CreditScore" : "EstimatedSalary" ]
y = data.loc[ :, 'Exited' ]

print()
print( f"x.shape = { x.shape }" )
print()
print( f"\nx.isnull().sum() :- \n{ x.isnull().sum() }" )
print( f"\ny.isnull().sum() :- \n{ y.isnull().sum() }\n" )

print( f"\nBefore Label Encoder, x.dtypes :- \n{ x.dtypes }" )
print( f"Before Label Encoder, x['Geography'].unique() = { x['Geography'].unique() }" )
print( f"Before Label Encoder, x['Gender'].unique() = { x['Gender'].unique() }" )

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

x['Geography'] = le.fit_transform( x['Geography'] )
x['Gender'] = le.fit_transform( x['Gender'] )

print( f"\nAfter Label Encoder, x.dtypes :- \n{ x.dtypes }" )
print( f"Before Label Encoder, x['Geography'].unique() = { x['Geography'].unique() }" )
print( f"Before Label Encoder, x['Gender'].unique() = { x['Gender'].unique() }" )

# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
#
# print( f"\nBefore Standard Scaler, x.head() :- \n{ x.head() }" )
# x = sc.fit_transform( x )
# print( f"\nAfter Standard Scaler, x :- \n{ x }" )

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2 )

print( f"x_train :- \n{ x_train }\n" )
print( f"x_test :- \n{ x_test }\n" )

from xgboost import XGBRFClassifier

#max_depth is the no. of levels in the tree
#Sub_sample is diving the train data
#colsample_by level represents in each level how many columns has to be taken
#n_estimators represents the no of epochs
#learning_rate represents the speed of learning
#learning_rate is inversaly proportional to accuracy and time also

xgboost = XGBRFClassifier( max_depth = 100, subsample=0.6, n_estimators = 500,learning_rate = 0.1  )

print( f"xgboost = { xgboost }" )

xgboost.fit( x_train, y_train )
y_pred = xgboost.predict( x_test )

print( f"xgboost.score( x_test, y_test ) = { xgboost.score( x_test, y_test ) * 100 }%" )

import matplotlib.pyplot as plt

plt.plot( x_test, y_test, label = 'Actual', marker = '*', color = 'blue', linestyle = '' )
plt.plot( x_test, y_pred, label = 'Prediction', marker = '+', color = 'red', linestyle = '' )
plt.legend()
plt.xlabel( 'x_test' )
plt.ylabel( 'y_test V/s y_pred' )
plt.title( 'XGBOOST' )
plt.show()