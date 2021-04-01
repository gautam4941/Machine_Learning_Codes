import numpy as np


x = np.array([1, 2, 3])
grid = np.array( [ [9, 8, 7], [6, 5, 4] ] )
y = np.array( [ [99],[98] ] )

print( f"x = { x }, x.shape = { x.shape }\n" )
print( f"grid = { grid }, grid.shape = { grid.shape }\n" )
print( f"y = { y }, y.shape = { y.shape }\n" )

print( np.vstack( [ x, grid ] ) )
print()
#print( np.vstack( [ grid, y ] ) )    #Error due to different column size
#print( np.hstack( [ x, grid ] ) )    #Error due to different row size
print( np.hstack( [ y, grid ] ) )
print()
print( np.hstack( [ grid, y ] ) )
print()


#########################split()###############

grid = np.arange(21).reshape( (3, 4) )
print( f"grid :- \n{ grid }\n" )

print( f"np.split(grid, [2]) :- \n{ np.split(grid, [2]) }\n" )

print( f"np.hsplit(grid, [2]) :- \n{ np.hsplit(grid, [2]) }\n" )

print( f"np.vsplit(grid, [2]) :- \n{ np.vsplit(grid, [2]) }\n" )