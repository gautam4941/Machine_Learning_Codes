import numpy as np

"""
arr1 = np.array( [ range(1, 11, 3)
                 , range(11, 21, 3)
                 , range(21, 31, 3) ] )

print( f"arr1 when dtype is not mentioned:- \n{ arr1 }" )
print( f"arr1.dtype = { arr1.dtype }\n" )
arr1.dtype = np.float16
print( f"arr1 when dtype = np.float16 :- \n{ arr1 }" )
print( f"arr1.dtype = { arr1.dtype }\n" )

arr2 = np.array( [ range(1, 11, 3)
                 , range(11, 21, 3)
                 , range(21, 31, 3) ], dtype = np.float64 )

print( f"arr2 when dtype = np.float64 :- \n{ arr2 }" )
print( f"arr2.dtype = { arr2.dtype }\n" )

arr3 = np.array( [ range(1, 11, 3)
                 , range(11, 21, 3)
                 , range(21, 31, 3) ], dtype = np.int32 )

print( f"arr3 when dtype = np.int32:- \n{ arr3 }" )
print( f"arr3.dtype = { arr3.dtype }\n" )
"""


arr1 = np.array( [ range(1, 11, 3)
                 , range(11, 21, 3)
                 , range(21, 31, 3) ] )

print( f"arr1 when dtype is not mentioned:- \n{ arr1 }" )
print( f"arr1.dtype = { arr1.dtype }\n" )

print( f"np.mean( arr1 ) = { np.mean( arr1 ) }\n" )

mean = np.mean( arr1, axis = 1 )   #Finding mean by row
print( f"mean when axis = 1 :- { mean }\n" )

mean = np.mean( arr1, axis = 0 )   #Finding mean by col
print( f"mean when axis = 0 :- { mean }\n" )

print( f"np.median( arr1 ) = { np.median( arr1 ) }" )
print()
print( f"np.median( arr1, axis= 1 ) = { np.median( arr1, axis= 1 ) }" )
print()
print( f"np.median( arr1, axis= 0 ) = { np.median( arr1, axis= 0 ) }" )
print()
print( f"np.sum( arr1) = { np.sum( arr1) }" )
print()
print( f"np.sum( arr1, axis = 1 ) = { np.sum( arr1, axis = 1 ) }" )
print()
print( f"np.sum( arr1, axis = 0 ) = { np.sum( arr1, axis = 0 ) }" )
