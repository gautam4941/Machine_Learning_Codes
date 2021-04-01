import pandas as pd

l1 = [200, 9000, 12, 67]
l2 = [2000, 900, 120, 670]

s1 = pd.Series( data = l1, index = ['one', 'two', 'three', 'four'] )
s2 = pd.Series( data = l2, index = ['one', 'two', 'three', 'four'] )
s3 = pd.Series( data = l2, index = ['one', 'two', 'three', 'five'] )

d2 = { 's1' : s1, 's2' : s2, 's3' : s3 }
pddf = pd.DataFrame( d2 )

print( f"pddf :- \n{ pddf }\n")

"""
# print( f"pddf['s1'] :- \n{ pddf['s1'] }\n" )
# print( f"pddf['s2'] :- \n{ pddf['s2'] }\n" )
# print( f"pddf['s3'] :- \n{ pddf['s3'] }\n" )
print()
print( f"pddf['s2'] + pddf['s3'] :- \n{ pddf['s2'] + pddf['s3'] }\n" )
print()

# add = []
# for i in range( len( pddf.index ) ):
#     #print( f"i = { i }, pddf['s1'][i] = { pddf['s1'][i] }, pddf['s2'][i] = { pddf['s2'][i] } and pddf['s1'][i] + pddf['s2'][i] = { pddf['s1'][i] + pddf['s2'][i] }" )
#     add.append( pddf['s1'][i] + pddf['s2'][i] )

#print( f"pd.Series( data=add )\n{ pd.Series( data=add, index = pddf.index ) }\n" )



#print( f"pddf['s2'] + pddf['s3'] :- \n{ pddf['s2'] + pddf['s3'] }\n" )


for i in range( len( pddf.index ) ):
    val1 = pddf['s2'][i]
    val2 = pddf['s3'][i]

    if( str( val1 ) == 'nan' ):
        val1 = 0

    if (str( pddf['s3'][i] ) == 'nan'):
        val2 = 0

    print( f"i = { i }, pddf['s2'][i] = { pddf['s2'][i] }, pddf['s3'][i] = { pddf['s3'][i] } and pddf['s2'][i] + pddf['s3'][i] = { val1+val2 }" )
"""

"""
print( f"pddf['s1'] - pddf['s2'] :- \n{ pddf['s1'] - pddf['s2'] }\n" )
print()
print( f"pddf['s1'] - pddf['s3'] :- \n{ pddf['s1'] - pddf['s3'] }\n" )
print()
print( f"pddf['s1'] * pddf['s3'] :- \n{ pddf['s1'] * pddf['s3'] }\n" )
"""

"""
print( f"pddf['s1'] > 100\n{ pddf['s1'] > 100 }\n" )
print()
print( f"pddf[ pddf['s1'] > 100 ] :- \n{ pddf[ pddf['s1'] > 100 ] }\n" )
print( f"pddf[ pddf['s1'] > 100 ]['s1'] :- \n{ pddf[ pddf['s1'] > 100 ]['s1'] }\n" )
print( f"pddf[ pddf['s1'] > 100 ]['s2'] :- \n{ pddf[ pddf['s1'] > 100 ]['s2'] }\n" )
print( f"pddf[ pddf['s1'] > 100 ]['s3'] :- \n{ pddf[ pddf['s1'] > 100 ]['s3'] }\n" )
"""

print( f"pddf :- \n{ pddf }\n" )
print( f"pddf['s1'] > 100 :- \n{ pddf['s1'] > 100 }\n" )
print( f"pddf[  ddf['s1'] > 100 ] :- \n{ pddf[ pddf['s1'] > 100 ] }\n" )
print( f"pddf['s1'] < 100 :- \n{ pddf['s1'] < 1000 }\n" )
print( f"pddf[ pddf['s1'] < 100 ] :- \n{ pddf[ pddf['s1'] < 1000 ] }\n" )
print( f"( pddf['s1'] > 100 ) & ( pddf['s1'] < 1000 ) :- \n{ ( pddf['s1'] > 100 ) & ( pddf['s1'] < 1000 ) }\n" )
print( f"pddf[ ( pddf['s1'] > 100 ) & ( pddf['s1'] < 1000 ) ] :- \n{ pddf[ ( pddf['s1'] > 100 ) & ( pddf['s1'] < 1000 ) ] }\n" )