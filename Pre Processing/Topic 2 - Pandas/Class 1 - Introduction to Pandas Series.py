#1. Creating Pandas Series
#2. Data and Index parameters
#3. n(index) = n(data)
#4. Mutability Checking -> Panda Series is Mutable

import pandas as pd

"""
list1 = list( range( 1, 6 ) )
list2 = list( range( 6, 11 ) )
list3 = list( range( 11, 16 ) )
list4 = list( range( 16, 21 ) )

print( f"list1 = { list1 }" )
print( f"list2 = { list2 }" )
print( f"list3 = { list3 }" )
print( f"list4 = { list4 }" )
print()

pds1 = pd.Series( list1 )
pds2 = pd.Series( list2 )
pds3 = pd.Series( list3 )
pds4 = pd.Series( list4 )

print( f"pds1 :- \n{ pds1 }\n" )
print( f"pds2 :- \n{ pds2 }\n" )
print( f"pds3 :- \n{ pds3 }\n" )
print( f"pds4 :- \n{ pds4 }\n" )
"""

"""
print( f"pd.Series( range( 1, 6 ) ) :- \n{ pd.Series( range( 1, 6 ) ) }\n" )

pds1 = pd.Series( range( 1, 6 ), [ 'a', 'b', 'c', 'd', 'e' ] )
print( f"pds1 :- \n{ pds1 }\n" )
print()
print( f"pds1[0] = { pds1[0] } and pds1['a'] = { pds1['a'] }" )
print( f"pds1[1] = { pds1[1] } and pds1['b'] = { pds1['b'] }" )
print( f"pds1[2] = { pds1[2] } and pds1['c'] = { pds1['c'] }" )
print( f"pds1[3] = { pds1[3] } and pds1['d'] = { pds1['d'] }" )
print( f"pds1[4] = { pds1[4] } and pds1['e'] = { pds1['e'] }" )
print()
pds2 = pd.Series( [ 'a', 'b', 'c', 'd', 'e' ], range( 1, 6 ) )
print( f"pds2 :- \n{ pds2 }\n" )
print()

##No of index = no of data
pds2 = pd.Series( index = [ 'a', 'b', 'c', 'd', 'e' ], data = range( 1, 6 ) )
print( f"pds2 :- \n{ pds2 }\n" )

#No of index > no of data
# pds2 = pd.Series( index = [ 'a', 'b', 'c', 'd', 'e', 'f' ], data = range( 1, 6 ) )
# print( pds2 )

#No of index < no of data
# pds2 = pd.Series( index = [ 'a', 'b', 'c', 'd' ], data = range( 1, 6 ) )
# print( pds2 )

#Mutability and Immutability
#Changing by integer/ numeric index
pds2[0] = 10
print()
print( f"After Changing pds2[0], pds2 :- \n{ pds2 }\n" )

#Changing by custom index
pds2['b'] = 20
print()
print( f"After Changing pds2['b'], pds2 :- \n{ pds2 }\n" )
"""

print( f"list( range( 1, 6 ) ) = { list( range( 1, 6 ) ) }" )
print( f"list( range( 1, 6 ) ) = { list( range( 6, 11 ) ) }" )
print( f"list( range( 1, 6 ) ) = { list( range( 11, 16 ) ) }" )
print( f"list( range( 1, 6 ) ) = { list( range( 16, 21 ) ) }" )
print()
pds2 = pd.Series( index = [ 'a', 'b', 'c', 'd' ], data = [ list( range( 1, 6 ) )
                                                         , list( range( 6, 11 ) )
                                                         , list( range( 11, 16 ) )
                                                         , list( range( 16, 21 ) ) ] )
print( f"pds2 :- \n{ pds2 }\n" )