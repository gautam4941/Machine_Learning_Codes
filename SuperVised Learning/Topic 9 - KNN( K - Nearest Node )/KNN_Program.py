import warnings
warnings.filterwarnings("ignore")
import pandas as pd

#Data Input
data = pd.read_csv(r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 9 - KNN( K - Nearest Node )\Iris.csv")
print( f"data:- \n{ data }\n" )

#Dividing Data into x and y
x = data.loc[ : , 'SepalLengthCm' : 'PetalWidthCm' ]
y = data.loc[ :, ['Species'] ]

print( f"x :- \n{ x }\n" )
print( f"y :- \n{ y }\n" )

#Checking the NUll value
print( f"x.isnull().sum() :- \n{ x.isnull().sum() }\n" )
print( f"y.isnull().sum() :- \n{ y.isnull().sum() }\n" )

#Data type checking, If String data then it must be converted into integer using Label Encoder
print( f"x.dtypes :- \n{ x.dtypes }\n" )
print( f"y.dtypes :- \n{ y.dtypes }\n" )

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

max_acc, max_i, max_n = 0, -1, -1

for i in range( 0, 21 ):	#i = 0, 1
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = i )  
	
	for j in range( 1, 8 ):		#i= 0 , j = 1
		model = KNeighborsClassifier( n_neighbors = j )		#model = KNeighborsClassifier( n_neighbors = j )
		model.fit( x_train, y_train)
		y_pred = model.predict( x_test )
		accuracy = accuracy_score( y_test, y_pred )
		
		# print( f"i = {i} and j = {j} and accuracy :- { accuracy }" )
		
		if( accuracy > max_acc ):
			max_acc = accuracy
			max_i = i
			max_n = j
			
			
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = max_i ) #and K = 4
			
error_rate = []
acc_rate = []
temp = x_test.copy()			#temp.row = 30
temp['y_test'] = y_test			#temp.row = 30


model = KNeighborsClassifier( n_neighbors = max_n )
model.fit( x_train, y_train)
y_pred = model.predict(x_test)		#x_test.rows = 30 and y_pred.row = 30
temp['y_pred'] = y_pred			#temp.row = 30

error_rate = np.mean( temp['y_test'] != temp['y_pred'] )
acc_rate = np.mean( temp['y_test'] == temp['y_pred'] )

import matplotlib.pyplot as plt

plt.plot( error_rate, color='red', linestyle='dashed', marker='o',markerfacecolor='orange', markersize=10, label = 'Error' )		 
plt.plot( acc_rate, color='green', linestyle='dashed',  marker='*',markerfacecolor='blue', markersize=10, label = 'Accuracy' )
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.legend()
plt.show()

plt.plot( temp['y_test'] , color = 'red', marker = '*', label = 'Actual', linestyle = '')
plt.plot( temp['y_pred'] , color = 'blue', marker = '+', label = 'Prediction', linestyle = '')
plt.legend()
plt.show()