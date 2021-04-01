import pandas as pd

"""
1) Data Deletion -> pop( index ), del
2) Data Insertion   -> a) Direct Method,  b) join()
"""

pds1 = pd.Series( data = list( range(1, 10, 2) ), index = ['one', 'three', 'five', 'seven', 'nine'] )
pds2 = pd.Series( data = list( range(10, 20, 2) ), index = [ 'ten', 'twelve', 'forteen', 'sixteen', 'eighteen' ] )
pds3 = pd.Series( data = list( range(20, 30, 2) ), index = ['twenty', 'twentytwo', 'twentyfour', 'twentysix', 'twentyeight' ] )
pds4 = pd.Series( data = list( range(20, 30, 2) ), index = ['twenty', 'twentytwo', 'twentyfour', 'twentysix', 'twentyeight' ] )
pds5 = pd.Series( data = list( range(10, 20, 1) ), index = [ 'ten', 'eleven', 'twelve', 'thirteen', 'forteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ] )
pds6 = pd.Series( data = list( range(20, 30, 1) ), index = ['twenty', 'twentyone', 'twentytwo', 'twentythree', 'twentyfour', 'twentyfive', 'twentysix', 'twentyseven', 'twentyeight',  'twentynine' ] )

d = { 'Series1' : pds1, 'Series2' : pds2, 'Series3' : pds3, 'Series4' : pds4, 'Series5' : pds5, 'Series6' : pds6  }
pddf = pd.DataFrame( d )

print( f"pddf :- \n{ pddf }\n" )

#Data Deletion

"""
        #pop
s6 = pddf.pop('Series6')

print()
print( s6 )
print()
print( pddf )
"""

"""
        #del
del pddf['Series5']   #del will do the action, Update the DataFrame and does not return any value
print( f"pddf :- \n{ pddf }\n" )
"""

"""
        #drop
        
#Delete specific rows :- pddf.drop( [ row1, row2, .., rown ], axis = 0 ) 

#Delete specific columns :- pddf.drop( [ col1, col2, .., coln ], axis = 1 ) 

"""

#Data Insertion - we are going to insert series1 data + 2.\n",
#There are 3 method to add data in existing DataFrame.

"""
#1) Direct Method, -> dataframe[ key/ new_col ] = panda Series
pddf['Series7'] = pddf['Series2'] + 10
print( f"pddf :- \n{ pddf }\n" )
"""

"""
#2) insert method - location + key(col_name) + data( panda Series )
#Syntax :- dataframe.insert( location, 'key', panda series )

pddf.insert( 2, 'Series7', pddf['Series2'] + 10 )
print( f"pddf :- \n{ pddf }\n" )
"""

"""
#3) join method - ( for join by default the location is last position in dataset )
#join() will do the action but not update pddf. So, we will have to save the action in pddf.
#syntax :- data_fram1.join( data_frame2 )

#series7 = pddf['Series2'] + 10

l = []
for i in pddf['Series2']:
    l.append( i )

series7 = pd.Series( data = l, index = pddf.index )

print( f"series7 :- \n{ series7 }\ntype( series7 ) :- \n{ type( series7 ) }\n" )

pds7 = pd.DataFrame( series7 )

pds7.columns = ['Series7']

print( f"pds7 :- \n{ pds7 }\ntype( pds7 ) :- \n{ type( pds7 ) }\n" )

pddf = pddf.join( pds7 )
print()
print( f"pddf = \n{ pddf }\n" )
"""