import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 14 - Classification Decision Tree\iris.csv" )
print( f"data :- \n{ data }\n" )

x = data.loc[ :, 'sepal_length' : 'petal_width' ]
y = data.loc[ :, 'species' ]

print( f"x :- \n{ x }" )
print( f"y :- \n{ y }" )

print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print( f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )

print( f"x.dtypes :- \n{ x.dtypes }\n" )
print( f"y.dtypes :- \n{ y.dtypes }\n" )

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2 )

print( f"x_train :- \n{ x_train }\n" )
print( f"x_test :- \n{ x_test }\n" )
print( f"y_train :- \n{ y_train }\n" )
print( f"y_test :- \n{ y_test }\n" )

print( f"x_train.shape = { x_train.shape }" )
print( f"y_train.shape = { y_train.shape }" )
print( f"x_test.shape = { x_test.shape }" )
print( f"y_test.shape = { y_test.shape }" )

from sklearn.preprocessing import StandardScaler
ssc = StandardScaler()
x_train = ssc.fit_transform( x_train )
x_test = ssc.fit_transform( x_test )

print( f"After Standard Scaler, x_train :- \n{ x_train }\n" )
print( f"After Standard Scaler, x_test :- \n{ x_test }\n" )

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier( criterion = 'entropy' )
print( f"dtc :- \n{ dtc }\n" )

dtc.fit( x_train, y_train )
y_pred = dtc.predict( x_test )

from sklearn.metrics import confusion_matrix
cm = confusion_matrix( y_test, y_pred )
print( f"cm :- \n{ cm }" )

accuracy = cm[0][0] + cm[1][1] + cm[2][2]

import numpy as np

total = np.sum( cm )
loss = total - accuracy

print( f"total = { total } and accuracy = { accuracy } and loss = { loss }" )

print( f"accuracy% = { accuracy/total }, loss% = { loss/total }\n" )

#Here, Prediction accuract will change as randomly data get allocated to train and test data.
print( f"dtc.score( x_test, y_test ) :- { dtc.score( x_test, y_test ) }" )

import matplotlib.pyplot as plt
plt.plot( x_test, y_test, color = 'blue', label = 'Actual', marker='*', markersize = 10,  linestyle = '' )
plt.plot( x_test, y_pred, color = 'red', label = 'Prediction', marker='*', markersize = 5, linestyle = '' )
plt.xlabel('x_test')
plt.ylabel('y-test')
plt.legend()

from sklearn.externals.six import StringIO
dot_data = StringIO()
print( f"dot_data = { dot_data }" )

from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

#export_graphviz(dtc)
#print()
#export_graphviz(dtc, out_file = dot_data)
#print()
#export_graphviz(dtc, out_file = dot_data, filled = True)
#print()
#export_graphviz(dtc, out_file = dot_data, filled = True, rounded = True)
#print()
export_graphviz(dtc, out_file = dot_data, filled = True, rounded = True, special_characters = True)

#Remove, all the arguments one by one and then, analyze the diffrence

#export_graphviz(dtc, out_file = dot_data,filled=True,rounded=True,special_characters=True)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue() )

print( f"Image(graph.create_png()) :- \n{ Image(graph.create_png()) }\n")