import pandas as pd

data = pd.read_csv('Social_Network_Ads.csv')
print( f"data :- \n{ data }\n" )

print( f"data.columns :- \n{ data.columns }\n" )

x = data.loc[ :, 'Gender' : 'EstimatedSalary' ]
y = data.loc[ :, 'Purchased' ]

print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print( f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )

print( f"x.dtypes :- \n{ x.dtypes }\n" )
print( f"y.dtypes :- \n{ y.dtypes }\n" )

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
x['Gender'] = le.fit_transform( x['Gender'] )

import  matplotlib.pyplot as plt
plt.plot( x['Age'], x['EstimatedSalary'], linestyle = '', marker = '*' )
plt.xlabel( 'Age' )
plt.ylabel( 'EstimatedSalary' )
plt.title( 'Age V/s Salary' )
plt.show()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2 )

from sklearn.decomposition import KernelPCA
kpca = KernelPCA( n_components = 2, kernel = 'rbf' )   #n_components is the number of columns getting trained

x_train = kpca.fit_transform( x_train )
x_test = kpca.fit_transform( x_test )

print( f"After Kernal PCA, x_train :- \n{ x_train }\n" )
print( f"After Kernal PCA, x_test :- \n{ x_test }\n" )

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

lr.fit( x_train, y_train )
y_pred = lr.predict( x_test )

new_x_test = x_test.T

plt.plot( x_test[0], x_test[1], linestyle = '', marker = '*' )
plt.xlabel( 'Age' )
plt.ylabel( 'EstimatedSalary' )
plt.title( 'Age V/s Salary' )
plt.show()

print( f"lr.score( x_test, y_test ) = { lr.score( x_test, y_test ) }" )