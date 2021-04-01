import pandas as pd

data =  pd.read_csv('winequality_red.csv')
print( f"data :- \n{ data }\n" )

x = data.loc[ :, 'fixed acidity' : 'alcohol' ]
y = data.loc[ :, 'quality' ]

print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print( f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size  = 0.3 )

print( f"x_train :- \n{ x_train }\nx_train.shape =  { x_train.shape }\n" )
print( f"y_train :- \n{ y_train }\n" )
print( f"x_test :- \n{ x_test }\n" )
print( f"y_test :- \n{ y_test }\ntype( y_test) =  { type( y_test) }\n" )

from sklearn.discriminant_analysis import  LinearDiscriminantAnalysis as LDA
lda = LDA( n_components = 4 )

x_train = lda.fit_transform( x_train, y_train )


print( f"After LDA, x_train :- \n{ x_train }\nx_train.shape =  { x_train.shape }\n" )
print( f"After LDA, y_train :- \n{ y_train }\n" )

x_test = lda.transform( x_test )

print( f"x_test :- \n{ x_test }\n" )


from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

lr.fit( x_train, y_train )
y_pred = lr.predict( x_test )

print( f"y_pred :- \n{ y_pred }" )
print( f"type( y_pred ) = { type( y_pred ) }" )

y_pred = pd.Series( y_pred )
print( f"y_pred.unique() = { y_pred.unique() }" )

import matplotlib.pyplot as plt
plt.plot( x_test, y_test, marker = '*', linestyle = '', color = 'red', label = 'y_test' )
plt.plot( x_test, y_pred, marker = '+', linestyle = '', color = 'blue', label = 'y_pred' )
plt.xlabel( 'X-TEST' )
plt.ylabel( 'Y_TEST V/s Y_PRED' )
plt.legend()
plt.show()
