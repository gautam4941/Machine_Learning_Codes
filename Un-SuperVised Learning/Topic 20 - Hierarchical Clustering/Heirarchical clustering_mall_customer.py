import pandas as pd

data = pd.read_csv( r'C:\Users\gauta\PycharmProjects\MachineLearning\Un-SuperVised Learning\Topic 20 - Hierarchical Clustering\Mall_Customers.csv' )

print( data.head() )

x = data.loc[ : , 'Gender' : 'Spending Score (1-100)' ]
print( x )
print()
print( "x.isnull().sum(),\n" )
print( x.isnull().sum() )
print()
print( "x.dtypes," )
print( x.dtypes )
print()
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

x['Gender'] = le.fit_transform( x['Gender'] )
print( x.head() )

# using the dendrogram to find optimal number of clusters
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

#ward method is used to mininmize varients
sch_list = sch.linkage( x , method='ward')
dendrogram= sch.dendrogram( sch_list )
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidena distances')
plt.show()

from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering( n_clusters = 3, affinity = 'euclidean', linkage = 'ward' )
y_hc=hc.fit_predict( x )

print( y_hc )

data['purchased'] = y_hc

print( data )


#visualising the cluster
plt.scatter(x[y_hc==0,0],x[y_hc==0,1],s=100,c='red',label='0 Category')
plt.scatter(x[y_hc==1,0],x[y_hc==1,1],s=100,c='blue',label='1 Category')
plt.scatter(x[y_hc==2,0],x[y_hc==2,1],s=100,c='green',label='2 Category')