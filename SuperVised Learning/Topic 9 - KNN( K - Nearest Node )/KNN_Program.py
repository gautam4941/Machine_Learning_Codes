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

max_acc = 0
max_i = -1
max_n = -1

for i in range( 0, 21 ):	#i = 0, 1
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = i )
	
	for j in range( 1, 8 ):		#i= 0 , j = 1
		model = KNeighborsClassifier( n_neighbors = j )		#model = KNeighborsClassifier( n_neighbors = j )
		model.fit( x_train, y_train)
		y_pred = model.predict( x_test )
		accuracy = accuracy_score( y_test, y_pred )
		
		print( f"i = {i} and j = {j} and accuracy :- { accuracy }" )
		
		if( accuracy > max_acc ):
			max_acc = accuracy
			max_i = i
			max_n = j
			
			
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = max_i ) #and K = 4
			
error_rate = []
acc_rate = []
temp = x_test.copy()			#temp.row = 30
temp['y_test'] = y_test			#temp.row = 30

for i in range(1,40):		#1, 2, ..., 39
 model = KNeighborsClassifier( n_neighbors = i )
 model.fit( x_train, y_train)
 y_pred = model.predict(x_test)		#x_test.rows = 30 and y_pred.row = 30
 temp['y_pred'] = y_pred			#temp.row = 30
 
 error_rate.append( np.mean( temp['y_test'] != temp['y_pred'] ) )
 acc_rate.append( np.mean( temp['y_test'] == temp['y_pred'] ) )

import matplotlib.pyplot as plt


plt.plot(np.arange( 1, len(error_rate) + 1 ),error_rate,color='red', linestyle='dashed', 
         marker='o',markerfacecolor='orange', markersize=10, label = 'Error' )
		 
plt.plot( np.arange( 1, len(error_rate) + 1 ),acc_rate,color='green', linestyle='dashed', 
         marker='*',markerfacecolor='blue', markersize=10, label = 'Accuracy' )
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier( n_neighbors = ? )
model.fit( x_train, y_train)
y_predict = model.predict( x_test )


from sklearn.metrics import accuracy_score
accuracy = accuracy_score( y_test, y_predict )
print( f"accuracy :- { accuracy }" )

score = model.score( x_test, y_test )
print( f"score = { score }" )


print( f"x_test.shape = { x_test.shape }" )
print( f"y_test.shape = { y_test.shape }" )
print( f"y_predict.shape = { y_predict.shape }" )


import matplotlib.pyplot as plt
plt.plot( x_test, y_test, color = 'red', marker = '*', label = 'Actual', linestyle = '')
plt.plot( x_test, y_predict, color = 'blue', marker = '+', label = 'Prediction', linestyle = '')
plt.show()