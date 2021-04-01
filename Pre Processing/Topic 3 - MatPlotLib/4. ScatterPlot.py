import matplotlib.pyplot as plt
import random

marks = []
for i in range(1, 51):  # 1, 2, .., 39, 40
    marks.append( random.randrange(1, 101, 10) )
print(f"marks = {marks} and len( marks ) = { len( marks ) }")

count = list( range( 1, 51 ) )
print( f"\ncount = { count } and len(count) = { len(count) }" )

plt.scatter( marks, count )
plt.xlabel( 'Roll Numbers -->' )
plt.ylabel( 'Counts -->' )
plt.title( 'Scatter Plot 1 - > Roll Numbers V/s Count' )
plt.show()

plt.scatter( count, marks )
plt.xlabel( 'Roll Numbers -->' )
plt.ylabel( 'Counts -->' )
plt.title( 'Scatter Plot 2 - > Roll Numbers V/s Count' )
plt.show()

plt.scatter( marks, count , label = 'Roll_no V/s Count')
plt.xlabel( 'Roll Numbers -->' )
plt.ylabel( 'Counts -->' )
plt.title( 'Scatter Plot 3 - > Roll Numbers V/s Count' )
plt.legend()
plt.show()

plt.scatter( marks, count , label = 'Roll_no V/s Count', color = 'red', marker = '*', s = 30)
plt.xlabel( 'Roll Numbers -->' )
plt.ylabel( 'Counts -->' )
plt.title( 'Scatter Plot 4 - > Roll Numbers V/s Count' )
plt.legend()
plt.show()

plt.scatter( marks, count , label = 'Roll_no V/s Count', color = 'red', marker = '*', s = 80 )
plt.xlabel( 'Roll Numbers -->' )
plt.ylabel( 'Counts -->' )
plt.title( 'Scatter Plot 4 - > Roll Numbers V/s Count' )
plt.legend()
plt.show()


plt.plot( marks, count , label = 'Roll_no V/s Count', color = 'red', marker = '*' )
plt.xlabel( 'Roll Numbers -->' )
plt.ylabel( 'Counts -->' )
plt.title( 'Plot 1 - > Roll Numbers V/s Count' )
plt.legend()
plt.show()

plt.plot( marks, count , label = 'Roll_no V/s Count', color = 'red', marker = '*', linestyle = '')
plt.xlabel( 'Roll Numbers -->' )
plt.ylabel( 'Counts -->' )
plt.title( 'Plot 2 - > Roll Numbers V/s Count' )
plt.legend()
plt.show()

#scatter_plot = plot + linestyle( '' )