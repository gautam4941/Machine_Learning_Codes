import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
print( f"x :- \n{ x }\n" )

"""
The axes (an instance of the class plt.Axes) is what we see above: a bounding
box with ticks and labels, which will eventually contain the plot elements that make
up our visualization.
"""
ax = plt.axes()
ax.plot(x, np.sin(x))
plt.show()


ax = plt.axes()
ax.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()


#We need to pass this projection as '3d' then, axes will form a 3d Graph
ax = plt.axes()
ax = plt.axes(projection='3d')
ax.plot()

#Show the remaining concept in Jupyter Notebook File