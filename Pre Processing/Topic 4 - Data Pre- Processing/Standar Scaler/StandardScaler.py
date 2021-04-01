import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\Pre Processing\Topic 4 - Data Pre- Processing\Standar Scaler\Data.csv" )
print( f"data :- \n{ data }\n" )

x = data.loc[ : , 'Age' : 'Salary' ]
print( f"x :- \n{ x }\n" )

from sklearn.preprocessing import StandardScaler
ssc = StandardScaler()

ssc_x = ssc.fit_transform( x )
print( f"ssc_x :- \n{ ssc_x }\n" )