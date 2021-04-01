import matplotlib.pyplot as plt

#Matplotlib is a library that we use basically to draw the graph and see the relationship
#among 2 or more datasets.


x = [1,2,3,4,5,6,7]
y = [50,51,52,48,47,49,46]

plt.plot( x, y )
plt.title("Only X and Y")
plt.show()

plt.plot( x, y, color = 'red' )
plt.title("X and Y, color")
plt.show()

plt.plot( x, y, color = 'red', marker = '*' )
plt.title("X and Y, color, marker")
plt.show()

plt.plot( x, y, color = 'red', marker = '*', linestyle = '' )
plt.title("X and Y, color, marker, linestyle")
plt.show()


plt.plot( x, y, color = 'red', marker = '*', linestyle = '--' )
plt.title("X and Y, color, marker, linestyle(--)")
plt.show()


plt.plot( x, y, color = 'red', linestyle = '--' )
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title( "Color + linestyle(--)" )
plt.show()

plt.plot( x, y, color = 'red', marker = '*', markersize = 20, linestyle = '--' )
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title( "Color + marker_size + linestyle(--)" )
plt.show()


x = [1,2,3,4,5,6,7]
y = [50,51,52,48,47,49,46]
z = [ 12000, 15000, 10000, 2000, 7000, 18000, 20000]

print( f"x = { x }" )
print( f"y = { y }" )
print( f"z = { z }" )

plt.plot( x, y, marker = '*', color = 'red' )
plt.plot( z, y, marker = 'o', color = 'blue' )
plt.xlabel('X and Z label')
plt.ylabel('Y label')
plt.title( "Color + marker_size" )
plt.show()

import numpy as np

x = np.linspace( 0, 10, 100 )

# end = 10, start = 0 -> end - start = 10-0 = 10/100 = 0.1
# [ 0. 0+0.1  0+0.1+0.1 0+0.1+0.1+0.1 ....]
# [ 0 0.1 0.2 0.3 ..... ]

print( f"x = { x } and len(x) = { len(x) }\n" )
print( f"np.cos(x) = { np.cos(x) } and len( np.cos(x) ) = { len( np.cos(x) ) }\n" )
print( f"np.sin(x) = { np.sin(x) } and len( np.sin(x) ) = { len( np.sin(x) ) }\n" )

plt.plot(x, np.sin(x), color = 'red', label = 'Sin function')
plt.plot(x, np.cos(x), color = 'blue', label = 'Cos function')
plt.legend()
plt.title( 'Sin() and Cos()' )
plt.show()


plt.subplot( 4, 1, 1 ) # (rows, columns, panel number)\n",
plt.plot( x, np.sin(x), label = 'Sin' )
plt.legend()
# create the second panel and set current axis\n",
plt.subplot( 4, 1, 4 )
plt.plot( x, np.cos(x), label = 'Cos' )
plt.legend()
plt.show()



plt.plot(x, x + 0, label = 'x + 0', linestyle='solid')
plt.plot(x, x + 1, label = 'x + 1', linestyle='dashed')
plt.plot(x, x + 2, label = 'x + 2', linestyle='dashdot')
plt.plot(x, x + 3, label = 'x + 3', linestyle='dotted')
# For short, you can use the following codes:
plt.plot(x, x + 4, label = 'x + 4', linestyle='-') # solid
plt.plot(x, x + 5, label = 'x + 5', linestyle='--') # dashed
plt.plot(x, x + 6, label = 'x + 6', linestyle='-.') # dashdot
plt.plot(x, x + 7, label = 'x + 7', linestyle=':') # dotted
plt.legend()
# plt.legend( loc = 'best' )
#plt.legend( loc = 'right' )
#plt.legend( loc = 'upper right' )
#plt.legend( loc = 'lower right' )
#plt.legend( loc = 'left' )
#plt.legend( loc = 'upper left' )
#plt.legend( loc = 'lower left' )
#plt.legend( loc = 'center' )
plt.show()
