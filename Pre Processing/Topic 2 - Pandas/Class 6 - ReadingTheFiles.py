import pandas as pd

#Read csv files
#syntax :- pd.read_csv( path )
csv_data = pd.read_csv( r'C:\Users\gauta\PycharmProjects\MachineLearning\Pre Processing\Topic 2 - Pandas\Excel Data\Book1.csv' )
print( f"csv_data :- \n{ csv_data }\n" )

#Read xlsx files
#syntax :- pd.read_excel( path )
xlsx_data = pd.read_excel( r"C:\Users\gauta\PycharmProjects\MachineLearning\Pre Processing\Topic 2 - Pandas\Excel Data\Book1.xlsx" )
print( f"xlsx_data :- \n{ xlsx_data }\n" )
print()

#checking Null values
print( f"csv_data.isnull() :- \n{ csv_data.isnull() }\n" )
print( f"csv_data.isnull().sum() :- \n{ csv_data.isnull().sum() }\n" )
print( f"xlsx_data.isnull().sum() :- \n{ xlsx_data.isnull().sum() }\n" )

#Fixing Null Values
#1) Filling one data for all,
    #syntax :- pandas_datafram.fillna( data )

print( f"csv_data.fillna( 5 ) :- \n{ csv_data.fillna( 5 ) }\n" )
#csv_data = csv_data.fillna( 5 )
print( f"csv_data :- \n{ csv_data }\n" )

#2) Filling all null data with their similar values
    #a) method = bfill :- backward fill
    #b) method = ffill :- forward fill

"""
print( f"csv_data.fillna( method = 'bfill' ) :- \n{ csv_data.fillna( method = 'bfill' ) }\n" )
#csv_data = csv_data.fillna( method = 'bfill' )
print( f"csv_data :- \n{ csv_data }\n" )
"""

"""
print( f"csv_data.fillna( method = 'bfill', axis = 1 ) :- \n{ csv_data.fillna( method = 'bfill', axis = 1 ) }\n" )
#csv_data = csv_data.fillna( method = 'bfill' )
print( f"csv_data :- \n{ csv_data }\n" )

print( f"csv_data.fillna( method = 'bfill', axis = 0 ) :- \n{ csv_data.fillna( method = 'bfill', axis = 0 ) }\n" )
#csv_data = csv_data.fillna( method = 'bfill' )
print( f"csv_data :- \n{ csv_data }\n" )
"""

"""
print( f"csv_data.fillna( method = 'bfill', axis = 'columns' ) :- \n{ csv_data.fillna( method = 'bfill', axis = 'columns' ) }\n" )
#csv_data = csv_data.fillna( method = 'bfill' )
print( f"csv_data :- \n{ csv_data }\n" )

print( f"csv_data.fillna( method = 'bfill', axis = 'rows' ) :- \n{ csv_data.fillna( method = 'bfill', axis = 'rows' ) }\n" )
#csv_data = csv_data.fillna( method = 'bfill' )
print( f"csv_data :- \n{ csv_data }\n" )
"""

"""
print( f"csv_data.fillna( method = 'ffill' ) :- \n{ csv_data.fillna( method = 'ffill' ) }\n" )
#csv_data = csv_data.fillna( method = 'ffill' )
print( f"csv_data :- \n{ csv_data }\n" )
"""

#Changing specific Nan values
print( f"csv_data.iloc[ 2, 1 ] :- \n{ csv_data.iloc[ 2, 1 ] }\n" )
csv_data.iloc[ 2, 1 ] = 'Mohan'
print( csv_data )