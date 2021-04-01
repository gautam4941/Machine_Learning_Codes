import pandas as pd

data = pd.read_csv(r'C:\Users\gauta\PycharmProjects\MachineLearning\Pre Processing\Topic 5 - Principle Component Analysis( PCA )\winequality_red.csv')
print( f"data :- \n{ data }\n" )

print( f"data.columns = { data.columns }\n" )

x = data.loc[ :, 'fixed acidity' : 'alcohol' ]
y = data.loc[ :, 'quality' ]

print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print( f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
x = ss.fit_transform( x )

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size  = 0.3 )

print( f"x_train :- \n{ x_train }\n" )
print( f"y_train :- \n{ y_train }\n" )
print( f"x_test :- \n{ x_test }\n" )
print( f"y_test :- \n{ y_test }\n" )

from sklearn.decomposition import PCA
pca = PCA( n_components = None )

x_train = pca.fit_transform( x_train )
x_test = pca.fit_transform( x_test )

print( f"x_train :- \n{ x_train }\nx_train.shape = { x_train.shape }" )
print( f"x_test :- \n{ x_test }\nx_test.shape = { x_test.shape }" )

variance_ratio = pca.explained_variance_ratio_
print( f"variance_ratio = { variance_ratio }\n" )


x_train, x_test, y_train, y_test = train_test_split( x, y, test_size  = 0.3 )

pca = PCA( n_components = None )
x_train = pca.fit_transform( x_train )
x_test = pca.fit_transform( x_test )

variance_ratio = pca.explained_variance_ratio_
print( f"After PCA, x_train :- \n{ x_train }\nx_train.shape = { x_train.shape }" )
print( f"After PCA, x_test :- \n{ x_test }\nx_test.shape = { x_test.shape }" )
print( f"variance_ratio = { variance_ratio }\n" )

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

lr.fit( x_train, y_train )
y_pred = lr.predict( x_test )

print( f"y_pred :- \n{ y_pred }" )
print( f"type( y_pred ) = { type( y_pred ) }" )

import matplotlib.pyplot as plt
plt.plot( x_test, y_test, marker = '*', linestyle = '', color = 'red', label = 'y_test' )
plt.plot( x_test, y_pred, marker = '+', linestyle = '', color = 'blue', label = 'y_pred' )
plt.xlabel( 'X-TEST' )
plt.ylabel( 'Y_TEST V/s Y_PRED' )
plt.legend()
plt.show()

y_pred = pd.Series( y_pred )
print( f"y_pred.unique() = { y_pred.unique() }" )