import pandas as pd

data = pd.read_csv(r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 8 - Naive Bayes\german_credit.csv")
print( f"data.head() :- \n{ data.head() }\n" )

print(f"data.columns :- \n{data.columns} and len( data.columns ) :- { len( data.columns ) }\n")
print( f"data['Creditability'].unique() :- { data['Creditability'].unique() }\n" )

y = data['Creditability']                    #y has only 'Creditability' column data.
x = data.loc[ :, 'Account Balance' :  ]      #x has 20 columns of data.

print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )

print( f"x.shape = { x.shape } and y.shape = { y.shape }\n" )


from sklearn.model_selection import train_test_split

#train_daata = 0.9 = 90% = 900 rows and test_data = 0.1 = 10% = 100 rows
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2 )

print( f"x_train :- \n{ x_train }\n" )
print( f"x_test :- \n{ x_test }\n" )
print( f"y_train :- \n{ y_train }\n" )
print( f"y_test :- \n{ y_test }\n" )

print( f"x_train.shape = { x_train.shape } and y_train.shape = { y_train.shape }\n" )
print( f"x_test.shape = { x_test.shape } and y_test.shape = { y_test.shape }\n" )

from sklearn.naive_bayes import GaussianNB   #Importing Library for Naive Bayes.

gnb = GaussianNB()                           #Making Object of GaussianNB class.

gnb.fit( x_train, y_train )                    #Giving training using x_train and y_train

y_pred = gnb.predict( x_test )                    #We are finding the new value. using predict().

#y_test is not used.
#y_test v/s new_y_test.

print( f"y_pred :- \n{ y_pred } and y_pred.shape = { y_pred.shape }\n" )

# To Find the Accuracy of our predicted data.
print( f"gnb.score(x_test, y_test) = { gnb.score(x_test, y_test) }" )

import matplotlib.pyplot as plt

plt.plot( x_test, y_test, color = 'blue', label = 'Actual', marker = '*', markersize = 10,  linestyle = '' )
plt.plot( x_test, y_pred, color = 'red', label = 'Precition', marker = '+', linestyle = '' )
plt.legend()
plt.show()

print( f"type( y_test ) :- { type( y_test ) } type( y_pred ) = { type( y_pred ) }\n" )

import numpy as np

y_test = np.array( y_test )
print( f"type( y_test ) :- { type( y_test ) } type( y_pred ) = { type( y_pred ) }\n" )

not_same = 0
same = 0

for i in range( len(y_test) ):
    if( y_test[i] != y_pred[i] ):
        not_same = not_same + 1
    else:
        same = same + 1

print( f"Same = { same } and not Same = { not_same }" )
print( f"InAccuracy = { not_same/len( y_pred ) }" )
print( f"Accuracy = { same/len( y_pred ) }\n" )