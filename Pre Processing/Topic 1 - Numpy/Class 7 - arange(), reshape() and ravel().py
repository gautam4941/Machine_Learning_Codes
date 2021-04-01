import numpy as np


print( f"np.arange(start = 3, stop = 7.1, step = 1) = { np.arange(start = 3, stop = 7.1, step = 1) }" )
print()
print( f"np.arange(start = 3, stop = 7.1 ) = { np.arange(start = 3, stop = 7.1 ) }" )
print()
print( f"np.arange(start = 3 ) = { np.arange( start = 3 ) }" )
print()
print( f"np.arange( 3 ) = { np.arange( 3 ) }" )
print()
print( f"np.arange( 3, 10 ) = { np.arange( 3, 10 ) }" )
print()
print( f"np.arange( 3,10, 2 ) = { np.arange( 3, 10, 2 ) }" )
print()
print( f"np.arange( 10, 1, -1 ) = { np.arange( 10, 1, -1 ) }" )
print()


arr1 = np.arange( 1, 10, 0.1 )
print( f"arr1 : { arr1 }\narr1.shape = { arr1.shape  }\n" )

arr2 = arr1.reshape( (3, 30) )
print( f"arr2 : { arr2 }\narr2.shape = { arr2.shape  }\n" )
print()

arr1 = np.array( [ range(1, 11), range( 11, 21 ) ] )
print( arr1, arr1.shape )
print()
arr1 = arr1.reshape( 4, 5 )
print( arr1, arr1.shape )
print()
arr1 = arr1.reshape( 2, 2, 5 )
print( arr1, arr1.shape )
print()
arr1 = arr1.ravel()
print( arr1, arr1.shape )
print()