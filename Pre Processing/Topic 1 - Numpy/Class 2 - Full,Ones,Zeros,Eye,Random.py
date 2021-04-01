#full(), zeros(), ones(), eye(), np.random.random(), np.random.randint(), np.random.seed()

import numpy as np

#Syntax :- np.full( shape, value )
arr = np.full( ( 2, 5 ), 3 )
print( f"arr = { arr }, type( arr) = { type( arr ) } and arr.dtype = { arr.dtype }" )
print()

#Syntax :- np.zeros( shape )
arr = np.zeros( ( 2, 5 ) )
print( f"arr = { arr }, type( arr) = { type( arr ) } and arr.dtype = { arr.dtype }" )

print()
#Syntax :- np.ones( shape )
arr = np.ones( ( 2, 5 ) )
print( f"arr = { arr }, type( arr) = { type( arr ) } and arr.dtype = { arr.dtype }" )
print()

#Syntax :- np.eye( shape1, shape2 )
print( "Eye Function :- \n" )
arr = np.eye( 5, 5 )
print( f"{ arr }, type( arr) = { type( arr ) }, arr.shape = { arr.shape } and arr.dtype = { arr.dtype }" )
print()

print( "np.random.random :- \n" )
#Syntax :- np.random.random( shape )
arrrandom = np.random.random( (2, 4, 3) )
print( arrrandom )
print()
print( f"type( arrrandom) = { type( arrrandom ) }, arrrandom.shape = { arrrandom.shape } and arrrandom.dtype = { arrrandom.dtype }" )

#Syntax :- np.random.randint( start, end, shape )
n1 = np.random.randint( 2, 10, 4 )
n2 = np.random.randint( 12, 20, 4 )
n3 = np.random.randint( 12, 20, ( 2, 5 ) )
n4 = np.random.randint( 12, 20, ( 2, 5, 3 ) )

print( f"n1 = { n1 }\n" )
print( f"n2 = { n2 }\n" )
print( f"n3 = { n3 }\n" )
print( f"n4 = { n4 }\n" )

#Syntax :- np.random.seed( seed_value )
print( f"1. Without Seed, np.random.randint( 2, 10, 4 ) = { np.random.randint( 2, 10, 4 ) }")
print( f"2. Without Seed, np.random.randint( 2, 10, 4 ) = { np.random.randint( 2, 10, 4 ) }")
print( f"3. Without Seed, np.random.randint( 2, 10, 4 ) = { np.random.randint( 2, 10, 4 ) }")

np.random.seed( 123223 )
print( f"4. With Seed, np.random.randint( 2, 10, 4 ) = { np.random.randint( 2, 10, 4 ) }")

print( f"5. Without Seed, np.random.randint( 2, 10, 4 ) = { np.random.randint( 2, 10, 4 ) }")

np.random.seed( 123223 )
print( f"6. With Seed, np.random.randint( 2, 10, 4 ) = { np.random.randint( 2, 10, 4 ) }")

np.random.seed( 123223 )
print( f"7. With Seed, np.random.randint( 2, 10, 4 ) = { np.random.randint( 2, 10, 4 ) }")