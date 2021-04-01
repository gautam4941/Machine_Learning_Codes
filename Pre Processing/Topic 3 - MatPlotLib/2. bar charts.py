"""
1) Single Bar Graph
2) MUlti Bar Graph.
3) Setting Width of Graph.
4) Setting the position of Bars( Left or right. )
5) Horizontal Bar Graph.

bar, barh, width, xaxis +/- value -> to shift the bar in the graph right/left respectively., xticks, yticks
"""

company = ['Google', 'Yahoo', 'Accenture', 'Philips']
revenue = [100, 50, 50, 10]

print( f"company = { company } and len( company ) = { len(company) }" )
print( f"revenue = { revenue } and len( revenue ) = { len(revenue) }" )

import numpy as np

xpos = np.arange( len( company ) )      #np.arange( 4 )    -> [ 0 1 2 3 ]

import matplotlib.pyplot as plt

#plt.plot( company, revenue, label = 'Revenue' )
plt.bar(company, revenue, label="Revenue")  #We are using bar instead of plot.
plt.xlabel("Companies")
plt.ylabel("Revenue(Bln)")
plt.title('US Technology Stocks')
plt.legend()
plt.show()


plt.bar(xpos, revenue, label= "Revenue")    #We are using bar instead of plot.\n",
plt.xticks(xpos,company)                #we use xticks to replace the x axis data. Syntax:- plt.xticks( old_X, new_X )\n",
plt.ylabel("Revenue(Bln)")
plt.title('US Technology Stocks')
plt.legend()
plt.show()


plt.bar(xpos, revenue, label="Revenue")
plt.xticks(xpos,company)
#plt.yticks( revenue, company )     #Matplot lib supports yticks also but, Some the Y data may get overlapped. Basically we use,
#xticks, ytticks to display the data valus( Number, String, etc ) instead of number ranging
plt.ylabel("Revenue(Bln)")
plt.title('US Technology Stocks')
plt.legend()
plt.show()
"""


profit=[40,2,34,12]

"""
plt.bar(company,revenue, label= "Revenue")
plt.bar(company,profit, label= "Profit")
plt.xlabel("Company")
plt.ylabel("Revenue(Bln) and Proit")
plt.title('US Technology Stocks')
plt.legend()
plt.show()

plt.bar(company,revenue, width=0.4, label= "Revenue")
plt.bar(company,profit, label= "Profit")
plt.xlabel("Company")
plt.ylabel("Revenue(Bln) and Proit")
plt.title('US Technology Stocks')
plt.legend()
plt.show()


plt.bar(company,revenue, width=0.4, label= "Revenue")
plt.bar(company,profit, width = 0.6, label= "Profit")
plt.xlabel("Company")
plt.ylabel("Revenue(Bln) and Proit")
plt.title('US Technology Stocks')
plt.legend()
plt.show()
"""

"""
xpos = np.arange( len( company ) )

plt.bar(xpos,revenue, width=0.4, label= "Revenue")
#plt.bar(xpos+0.2,profit, width = 0.6, label= "Profit")
plt.xticks( xpos, company )
plt.xlabel("Company")
plt.ylabel("Revenue(Bln) and Proit")
plt.title('US Technology Stocks')
plt.legend()
plt.show()
"""

"""
plt.barh(xpos,revenue, label= "Revenue")
# .bar() -> is for Displaying the bar Horizontally( alignment w.r.t to y axis )
#Whereas, .barh() ->  To display bars vertically( alignment w.r.t to x axis)
plt.yticks(xpos,company)
plt.xlabel( 'Stocks' )
plt.ylabel("Revenue(Bln)")
plt.title('US Technolog Stocks')
plt.legend()
plt.show()
"""