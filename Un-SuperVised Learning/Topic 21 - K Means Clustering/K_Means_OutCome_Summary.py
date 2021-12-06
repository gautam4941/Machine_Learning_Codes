import pandas as pd

data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\Un-SuperVised Learning\Topic 21 - K Means Clustering\KMEANS_OUTCOME.csv" )

spending_categories = [0, 0, 0, 0, 0]
spending_count = [0, 0, 0, 0, 0]

for i in range( len( data ) ):
	spending_categories[ data['Purchased'][i] ] = spending_categories[ data['Purchased'][i] ] + data['Spending Score (1-100)'][i]
	spending_count[ data['Purchased'][i] ] = spending_count[ data['Purchased'][i] ] + 1

print( f"spending_categories = { spending_categories }" )
print( f"spending_count = { spending_count }" )


Highest_Mean = 0
Highest_Category = -1

for i in range( len( spending_categories ) ):
    curr_mean = spending_categories[i]/spending_count[i]

    print( f"curr_mean = { curr_mean }" )

    if( curr_mean > Highest_Mean ):
        Highest_Mean = curr_mean
        Highest_Category = i

print()
print( f"Highest_Mean = { Highest_Mean }" )
print( f"Highest_Category = { Highest_Category }" )