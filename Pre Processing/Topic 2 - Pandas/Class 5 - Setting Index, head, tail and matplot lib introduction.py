import pandas as pd

l1 = ['Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sar', 'Sun']
l2 = [8, 6, 9, 4, 1, 0]
l3 = [2, 1, 1, 2, 0, 3]
l4 = [2, 2, 4, 3, 0, 2]
l5 = [6, 8, 6, 7, 4, 9]

pds1 = pd.Series( l1 )
pds2 = pd.Series( l2 )
pds3 = pd.Series( l3 )
pds4 = pd.Series( l4 )
pds5 = pd.Series( l5 )

d = {'Days' : pds1, 'Studying' : pds2, 'Television' : pds3, 'Playing' : pds4, 'Sleeping' : pds5}

pddf = pd.DataFrame( d )

print( f"pddf :- \n{ pddf }\n" )
temp = pddf.copy()

"""
print( f"temp :- \n{ temp }\n" )

temp.index = temp['Days']

print( f"pddf :- \n{ pddf }\n" )
print()
print( f"temp :- \n{ temp }\n" )
temp.pop( 'Days' )
print( f"temp :- \n{ temp }\n" )
"""

"""
#set_index
print( f"temp :- \n{ temp }\n" )

temp.set_index('Days' )

print( f"temp :- \n{ temp }\n" )

temp.set_index('Days', inplace= False )

print( f"temp :- \n{ temp }\n" )

temp.set_index('Days', inplace = True )

print( f"temp :- \n{ temp }\n" )
"""

"""
#head() and tail()
print( f"pddf.head() :- \n{ pddf.head() }\n" )
print( f"pddf.head(10) :- \n{ pddf.head(10) }\n" )
print( f"pddf.head(2) :- \n{ pddf.head(2) }\n" )
print()
print( f"pddf.tail() :- \n{ pddf.tail() }\n" )
print( f"pddf.tail(10) :- \n{ pddf.tail(10) }\n" )
print( f"pddf.tail(2) :- \n{ pddf.tail(2) }\n" )
"""