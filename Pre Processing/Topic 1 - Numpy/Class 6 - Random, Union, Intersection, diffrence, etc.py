import numpy as np

arr1 = np.array( [ range(1, 11, 3)
                 , range(11, 21, 3)
                 , range(21, 31, 3) ] )

print( f"arr1 :- \n{ arr1 }\n" )

arr2 = np.array( [ range(1, 11, 3)
                 , range(31, 41, 3)
                 , range(41, 51, 3) ] )

print( f"arr2 :- \n{ arr2 }\n" )

print( f"arr1.ravel() = { arr1.ravel() }\n" )
print( f"arr2.ravel() = { arr2.ravel() }\n" )

print( f"np.intersect1d( arr1, arr2 ) :- \n{ np.intersect1d( arr1, arr2 ) }\n " )


print( f"np.union1d( arr1, arr2 ) :- \n{ np.union1d( arr1, arr2 ) }\n" )

print( f"np.setdiff1d( arr1, arr2 ) :- \n{ np.setdiff1d( arr1, arr2 ) }\n" )

print( f"np.setdiff1d( arr2, arr1 ) :- \n{ np.setdiff1d( arr2, arr1 ) }\n" )

print( f"np.in1d( arr2, arr1 ) :- \n{ np.in1d( arr2, arr1 ) }\n" )

print( f"arr2[ np.in1d( arr2, arr1 ) ] :- \n{ arr2[ np.in1d( arr2, arr1 ) ] }\n" )