import numpy as np

x = np.arange( 1, 6 )
y = np.arange( 11, 14 )

print( f"x = { x }" )
print()
print( f"y = { y }\n" )

print( f"np.meshgrid( x, y ) :- \n{ np.meshgrid( x, y ) }\n" )

print( f"np.meshgrid( y, x ) :- \n{ np.meshgrid( y, x ) }\n" )
print()

z = np.array( [ range(21, 26), range( 26, 31 ) ] )
print( f"z :- \n{ z }" )
print()
print( f"np.meshgrid( x, z ) :- \n{ np.meshgrid( x, z ) }\n" )