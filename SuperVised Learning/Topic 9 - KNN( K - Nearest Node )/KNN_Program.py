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
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0 )

print( f"x_train :- \n{ x_train }\n" )
print( f"y_train :- \n{ y_train }\n" )
print( f"x_test :- \n{ x_test }\n" )
print( f"y_test :- \n{ y_test }\n" )

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier( n_neighbors = 5 )
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