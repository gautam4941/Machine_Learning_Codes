import pandas as pd
pd.set_option('display.max_columns', None)

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\Recursive Feature Elimination (RFE)\breast_cancer_data.csv" )
print( data )

x = data.loc[ :, 'mean radius' : 'worst fractal dimension' ]
y = data.loc[ :, 'Cancer' ]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2, random_state = 0 )

print( f"x_train :- \n{ x_train }\n" )
print( f"x_test :- \n{ x_test }\n" )

print( f"x_train.shape = { x_train.shape }" )
print( f"x_test.shape = { x_test.shape }\n" )

################################Feature_Selection######################

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel

#remove random_state and then see the difference in sel.get_support()
sel = SelectFromModel( RandomForestClassifier( n_estimators = 100, random_state = 0 ) )
sel.fit( x_train, y_train )

print( f"sel.get_support() :- \n{ sel.get_support() }\n" )
print( f"len( sel.get_support() ) :- \n{ len( sel.get_support() ) }\n" )

sel_columns = x_train.columns[ sel.get_support() ]
print( f"sel_columns :- \n{ sel_columns }\nlen( sel_columns ) :- { len( sel_columns ) }\n" )

sel_feature_importance = sel.estimator_.feature_importances_
print( f"sel_feature_importance :- \n{ sel_feature_importance }\n" )
import numpy as np
print( f"np.sum( sel_feature_importance ) :- { np.sum( sel_feature_importance ) }\n" )

sel_columns_mean = np.mean( sel_feature_importance )
print( f"sel_columns_mean :- { sel_columns_mean }" )
print( f"sel.get_support() :- \n{ sel.get_support() }\n" )

def run_random_forest( x_train, y_train, x_test, y_test ):
    rf = RandomForestClassifier( n_estimators = 100, random_state = 0 )
    rf.fit( x_train, y_train )
    return rf.score( x_test, y_test )

print( "Normal Random Forest :- ", run_random_forest( x_train, y_train, x_test, y_test ) )

sel_x_train = sel.transform( x_train )
sel_x_test = sel.transform( x_test )

print( "Random Forest with SelectFromModel :- ", run_random_forest( sel_x_train, y_train, sel_x_test, y_test ) )

################################Recursive Feature Elimination (RFE)######################

from sklearn.feature_selection import RFE
#rfe = RFE( RandomForestClassifier( n_estimators = 100, random_state = 0 ), n_features_to_select = 10 )

rfe = RFE( RandomForestClassifier( n_estimators = 100, random_state = 0 ) )
rfe.fit( x_train, y_train )

print( f"Total columns :- { x_train.columns }\n" )
print( f"rfe.get_support() = { rfe.get_support() }\n" )

rfe_columns = x_train.columns[ rfe.get_support() ]
print( f"RFE columns :- { rfe_columns }\n len( rfe_columns ) = { len( rfe_columns ) }\n" )

rfe_x_train = rfe.transform( x_train )
rfe_x_test = rfe.transform( x_test )


print( f"Normal Random Forest, Accuracy :- { run_random_forest( x_train, y_train, x_test, y_test ) }" )
print( f"Random Forest with SelectFromModel, Accuracy :- { run_random_forest( sel_x_train, y_train, sel_x_test, y_test ) }" )
print( f"Random Forest with RFE, Accuracy :- { run_random_forest( rfe_x_train, y_train, rfe_x_test, y_test ) }\n" )

#Now change the n_features_to_select and see the accuracy

rfe_accuracy_list = []

for i in range( 1, len( x_train.columns )+1 ):
    rfe = RFE( RandomForestClassifier( n_estimators = 100, random_state = 0 ), n_features_to_select = i )
    rfe.fit(x_train, y_train)
    rfe_x_train = rfe.transform(x_train)
    rfe_x_test = rfe.transform(x_test)
    accuracy = run_random_forest(rfe_x_train, y_train, rfe_x_test, y_test)
    print(f"Random Forest {i} with RFE, Accuracy :- ", accuracy )
    rfe_accuracy_list.append( accuracy )

print()
print( f"rfe_accuracy_list :- { rfe_accuracy_list }" )

rfe = RFE( RandomForestClassifier( n_estimators = 100, random_state = 0 ), n_features_to_select = 17 )
rfe.fit(x_train, y_train)
rfe_x_train = rfe.transform(x_train)
rfe_x_test = rfe.transform(x_test)
accuracy = run_random_forest(rfe_x_train, y_train, rfe_x_test, y_test)
print(f"Random Forest {i} with RFE, Accuracy :- ", accuracy )


print( f"Columns selected in RFE when n_features_to_select = 17, { x_train.columns[ rfe.get_support() ] }\n" )

