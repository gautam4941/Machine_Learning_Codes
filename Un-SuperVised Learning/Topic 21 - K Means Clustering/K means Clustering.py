import  pandas as pd

data = pd.read_csv( r'C:\Users\gauta\PycharmProjects\MachineLearning\Un-SuperVised Learning\Topic 21 - K Means Clustering\Customers.csv' )
print( data.head() )
print()
x = data.loc[ : , 'Gender' : 'Spending Score (1-100)' ]
print( "x.isnull().sum()," )
print( x.isnull().sum() )
print()
print( x.dtypes )

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

x['Gender'] = le.fit_transform( x['Gender'] )

print()
print( x.head() )

from sklearn.cluster import KMeans

l = []
max_no_of_centroid = 50
for i in range( 1, max_no_of_centroid + 1 ):        # i = 1, 2, 3, 4, ..
    km = KMeans( n_clusters = i )   # n_clusters = 1, 2, 3, 4, ...
    #print( km )
    km.fit( x )                     # Training
    print()
    print( f"i = { i } and km.inertia_ = { km.inertia_ }" )
    l.append( km.inertia_ )

print( f"km.inertia_ list = { l }" )

import matplotlib.pyplot as plt
plt.plot( range(1, max_no_of_centroid + 1), l, marker = '*' )      # range( 1, 20 ), l
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

idle_cluster = int( input("Enter the Cluster number = ") )

km = KMeans( n_clusters = idle_cluster )
km.fit( x )
y_pred = km.predict( x )

print( y_pred )

data['Purchased'] = y_pred

print( f"data :- \n{ data }\n" )

data.to_csv( r'C:\Users\gauta\PycharmProjects\MachineLearning\Un-SuperVised Learning\Topic 21 - K Means Clustering\KMEANS_OUTCOME.csv' )



for i in range( 0, idle_cluster ):
    temp = x[x.Purchased == i ]
    plt.scatter( temp.Age, temp['Annual Income (k$)'], label = f"{i}_Cat" )

plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5);
plt.legend()
plt.title( 'K MEANS' )
plt.xlabel( 'AGE' )
plt.ylabel( 'INCOME' )
plt.show()