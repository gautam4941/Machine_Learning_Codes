import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 15 - Classification Random Forest\Social_Network_Ads.csv" )

print( f"data.shape = { data.shape } and data.columns = { data.columns }" )
print()

x = data.loc[ :, 'Gender' : 'EstimatedSalary' ]
print( f"x.shape = {x.shape} and x.columns = { x.columns }" )
print()
y = data.loc[ :, ['Purchased'] ]
print( f"y.shape = {y.shape} and y.columns = { y.columns }" )
print()

print( "x.isnull().sum()\n", x.isnull().sum() )
print()
print( "y.isnull().sum()\n", y.isnull().sum() )
print()
print( "x.dtypes\n", x.dtypes )
print()
print( "y.dtypes\n", y.dtypes )
print()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

print( f"x['Gender'].unique() = { x['Gender'].unique() }" )
print()
x['Gender'] = le.fit_transform( x['Gender'] )
print( f"x['Gender'].unique() = { x['Gender'].unique() }" )

from sklearn.preprocessing import StandardScaler
ssc = StandardScaler()
x = ssc.fit_transform( x )

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2 )  #train_data = 0.8 = 80% = 320 rows

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit( x_train, y_train )

y_pred = rfc.predict( x_test )

print( y_pred )

print( f"rfc.score( x_test, y_test ) = { rfc.score( x_test, y_test ) }")

from sklearn.metrics import confusion_matrix
cm = confusion_matrix( y_test, y_pred )
print( cm )

accuracy = cm[0][0] + cm[1][1]
inaccuracy = cm[0][1] + cm[1][0]

print( f"Accuracy = { accuracy } and accuracy% = { ( accuracy/len( y_test ) ) * 100 }" )
print( f"InAccuracy = { inaccuracy } and inaccuracy% = { ( inaccuracy/len( y_test ) ) * 100 }" )
