import pandas as pd

pds1 = pd.Series( data = list( range( 1, 6 ) ) )
pds2 = pd.Series( data = list( range( 6, 11 ) ) )
pds3 = pd.Series( data = list( range( 11, 16 ) ) )
pds4 = pd.Series( data = list( range( 16, 20 ) ) )

d = { 'col1' : pds1
     ,'col2' : pds2
     ,'col3' : pds3
     ,'col4' : pds4 }

pdf1 = pd.DataFrame( d )

print( pdf1 )
print()

print( f"pdf1[ 'col2' ]\n{ pdf1[ 'col2' ] }" )  #pdf1[ 'col2' ] = pds1
print()
print( f"pdf1[ 'col4' ]\n{ pdf1[ 'col4' ] }\n{ len( pdf1['col4'] ) }" )  #pdf1[ 'col2' ] = pds1
print()
print( f"pds4\n{ pds4 }\n{ len( pds4 ) }" )
print()

#Mutability Test
pdf1[ 'col4' ] = [6, 9, 10, 11, 56 ]

print( pdf1 )
print()
print( f"id( pdf1 ) = { id( pdf1 ) }, id( d ) = { id( d ) } and id( pds4 ) = { id( pds4 ) }" )
print()

#loc() and iloc()
#Syntax :- data_frame_name.loc[ row1 : row2 , col1 : col2 ]
#Syntax :- data_frame_name.iloc[ integer_row1 : integer_row2 , integer_col1 : integer_col2 ]

print( f"pdf1.loc[ : , : ]\n{ pdf1.loc[ : , : ] }" )
print()
print( f"pdf1.loc[ 2 : , : ]\n{ pdf1.loc[ 2 : , : ] }" )
print()
print( f"pdf1.loc[ 2 : 4 , : ]\n{ pdf1.loc[ 2 : 4 , : ] }" )
print()
print( f"pdf1.loc[ 2 : 4 , 'col2' : ]\n{ pdf1.loc[ 2 : 4 , 'col2' : ] }" )
print()
print( f"pdf1.loc[ 2 : 4 , 'col2' : 'col4' ]\n{ pdf1.loc[ 2 : 4 , 'col2' : 'col4' ] }" )
print()
print( f"pdf1.loc[ 2 : 4 , 'col2' : 'col3' ]\n{ pdf1.loc[ 2 : 4 , 'col2' : 'col3' ] }" )
print()
print( f"pdf1.iloc[ 2 : 4 , 1 : 3 ]\n{ pdf1.iloc[ 2 : 4, 1 : 3 ] }" )
print()


"""
# pds1 = pd.Series( data = list( range(1, 10, 2) ), index = ['one', 'three', 'five', 'seven', 'nine'] )
# pds2 = pd.Series( data = list( range(10, 20, 2) ), index = [ 'ten', 'twelve', 'forteen', 'sixteen', 'eighteen' ] )
# pds3 = pd.Series( data = list( range(20, 30, 2) ), index = ['twenty', 'twentytwo', 'twentyfour', 'twentysix', 'twentyeight' ] )
# pds4 = pd.Series( data = list( range(1, 10, 1) ), index = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] )
# pds5 = pd.Series( data = list( range(10, 20, 1) ), index = [ 'ten', 'eleven', 'twelve', 'thirteen', 'forteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ] )
# pds6 = pd.Series( data = list( range(20, 30, 1) ), index = ['twenty', 'twentyone', 'twentytwo', 'twentythree', 'twentyfour', 'twentyfive', 'twentysix', 'twentyseven', 'twentyeight',  'twentynine' ] )

pds1 = pd.Series( data = list( range(1, 10, 2) ) )
pds1 = pd.Series( data = list( range(1, 10, 2) ) )
pds2 = pd.Series( data = list( range(10, 20, 2) ) )
pds3 = pd.Series( data = list( range(20, 30, 2) ) )
pds4 = pd.Series( data = list( range(1, 100, 1) ) )
pds5 = pd.Series( data = list( range(10, 20, 1) ) )
pds6 = pd.Series( data = list( range(20, 30, 1) ) )

print( f"pds1\n{ pds1 }\n" )
print( f"pds2\n{ pds2 }\n" )
print( f"pds3\n{ pds3 }\n" )
print( f"pds4\n{ pds4 }\n" )
print( f"pds5\n{ pds5 }\n" )
print( f"pds6\n{ pds6 }\n" )

d = { 'pds1' : pds1
     ,'pds2' : pds2
     , 'pds3': pds3
     , 'pds4': pds4
     , 'pds5': pds5
     , 'pds6': pds6}

pdf1 = pd.DataFrame( d )

print( f"pdf1\n{ pdf1 }\n" )
"""

#arr[row1 : row2, col1 : col2 ]

print()
print( pds2.iloc[ 1 : 3 ] )
print()
print( pds2.loc[ 'b' : 'c' ] )
print()
print( pds2.iloc[ [1, 3] ] )
print()
print( pds2.loc[ ['b', 'd'] ] )
print()