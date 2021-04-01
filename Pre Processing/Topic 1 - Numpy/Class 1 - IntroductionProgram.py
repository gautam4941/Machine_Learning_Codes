#How to create numpy array
#Mutability and Immutability

import numpy as np

l = [ [5, 6, 9, 10, 11], [ 1, 2, 3, 5, 6 ] ]
print( l, type(l), len(l) )

arr = np.array( l )
print( f"arr = { arr }", type( arr ), len( arr ), arr.shape )
print()

print( "Printing Numpy Array in the loop" )
for i in arr:
    print( f"i : { i }" )

    for j in i:
        print( f"    j : {j}" )


print()
arr[1] = 9
print( "Checking Mutability, " )
print( f"arr = { arr }" )
arr[1][3] = 5
print( f"arr = { arr }" )
print()