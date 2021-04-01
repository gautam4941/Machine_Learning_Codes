import numpy as np

"""
arr = np.array( [ range(0, 10, 3)
                , range(10, 20, 3)
                , range(20, 30, 3) ] )

print( f"arr :- \n{ arr }\n arr.shape :- { arr.shape }\n" )

new_arr1 = arr > 15
print( f"new_arr1 :- \n{ new_arr1 }\n and new_arr1.shape = { new_arr1.shape }" )
print()
new_arr1 = arr[ new_arr1 ]
print( f"new_arr1 :- \n{ new_arr1 }\n and new_arr1.shape = { new_arr1.shape }" )

temp = new_arr1 < 25
print( f"temp = { temp } and temp.shape = { temp.shape }\n" )

new_arr1 = new_arr1[temp]
print( f"new_arr1 = { new_arr1 } and new_arr1.new_arr1 = { new_arr1.shape }\n" )
"""


arr = np.array( [ range(0, 10, 3)
                , range(10, 20, 3)
                , range(20, 30, 3) ] )

print( f"arr :- \n{ arr }\n arr.shape :- { arr.shape }\n" )
print()
new_arr1 = arr[ arr>15 ]
print( f"new_arr1 :- \n{ new_arr1 }\n and new_arr1.shape = { new_arr1.shape }" )
print()
print( new_arr1[ new_arr1 < 26 ] )
print()
print( f"new_arr1 :- \n{ new_arr1 }\n and new_arr1.shape = { new_arr1.shape }" )
print()
print( f"arr%2 :- \n{ arr%2 }\n" )

print( arr[ arr%2 == 0 ] )
print()
print( f"arr :- \n{ arr }\n and arr.shape = { arr.shape }\n" )

print( f"arr + 2 :- \n{  arr + 2}\n" )

print( f"arr - 2 :- \n{  arr - 2}\n" )

print( f"arr * 2 :- \n{  arr * 2}\n" )

print( f"arr / 2 :- \n{  arr / 2}\n" )

print( f"arr // 2 :- \n{  arr // 2}\n" )