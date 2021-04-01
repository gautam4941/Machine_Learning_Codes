import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\Pre Processing\Topic 2 - Pandas\Excel Data\Social_Network_Ads.csv" )

print( f"data.head() :- \n{ data.head() }\ndata.shape :- { data.shape }\n" )

#Syntax :-  pd.get_dummies( column_name )
print( f"pd.get_dummies( data['Gender'] ) :- \n{ pd.get_dummies( data['Gender'] ) }\n" )

#Storing get_dummies value into a variable and then, we will concatinate the dummy_data with our dataset

gender_dummy = pd.get_dummies( data['Gender'] )
print( f"gender_dummy :- \n{ gender_dummy }\n\ntype( gender_dummy ) :- \n{ type( gender_dummy ) }" )

print( f"data.join( gender_dummy ) :- \n{ data.join( gender_dummy ) }\n" )
data = data.join( gender_dummy )
print( f"data :- \n{ data }\n" )


#loc
x = data.loc[ :, 'Age' : 'Male' ]
print( f"x :- \n{ x }\n" )

x = data.loc[ :, ['Age', 'EstimatedSalary', 'Female', 'Male' ] ]
print( f"x :- \n{ x }\n" )

print( f"data['EstimatedSalary'].unique() :- \n{ data['EstimatedSalary'].unique() }\n" )
print( f"len( data['EstimatedSalary'].unique() ) :- { len( data['EstimatedSalary'].unique() ) }\n" )
print( f"type( data['EstimatedSalary'].unique() ) = { type( data['EstimatedSalary'].unique() ) }\n" )
print( f"data['EstimatedSalary'].unique().shape :- { data['EstimatedSalary'].unique().shape }\n" )

gender_dummy = pd.get_dummies( data['EstimatedSalary'] )
print( f"gender_dummy :- \n{ gender_dummy }\n\ntype( gender_dummy ) :- \n{ type( gender_dummy ) }" )