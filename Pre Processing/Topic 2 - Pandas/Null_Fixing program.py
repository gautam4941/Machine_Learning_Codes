def null_check( data_frame ):
    import numpy as np
    import statistics as st
    df_dict = data_frame.isnull().sum()
    
    null_col = []
    remove_col = []
    
    for key, val in df_dict.items():
        if( val > 0 ):
            null_col.append( key )
            if( ( val/data_frame.shape[0] ) > 0.4 ):
                data_frame = data_frame.drop( key, axis = 1 )
                remove_col.append( key )
                
    print(f"Total Null columns are :- { null_col }")
    print(f"Total removed columns are :- { remove_col }\n")
    
    for i in remove_col:
        null_col.remove( i )
        
    for i in null_col:
        if( data_frame[ i ].dtypes == 'object'):
            print( f"Column : { i } has following unique values : \n { data_frame[i].value_counts() }" )
            
            op = int( input( f"Columns_name = {i}, Fix values by, 1. Mode, 2. Bfill, 3.FFill, 4.Other = " ) )
            
            if( op == 1 ):
                data_frame[ i ] = data_frame[ i ].fillna( st.mode( data_frame[ i ] ) )
            elif( op == 2 ):
                data_frame[ i ] = data_frame[ i ].fillna( method = 'bfill' )
                
            elif( op == 3 ):
                data_frame[ i ] = data_frame[ i ].fillna( method = 'ffill' )
                
            elif( op == 4):
                
                data_frame[ i ] = data_frame[ i ].fillna( input("Enter data to be filled at null places = ") )
            else:
                print( "Wrong Input. Try Again !")
        
        else:
            op = int( input( f"Columns_name = {i}, Fix values by, 1. Mode, 2.Mean,  3.Bfill, 4.FFill, 5.Other = " ) )
            
            if( op == 1 ):
                data_frame[ i ] = data_frame[ i ].fillna( st.mode( data_frame[ i ] ) )
                
            elif( op == 2 ):
                data_frame[ i ] = data_frame[ i ].fillna( np.mean( data_frame[ i ] ) )
            
            elif( op == 3 ):
                data_frame[ i ] = data_frame[ i ].fillna( method = 'bfill' )
                
            elif( op == 4 ):
                data_frame[ i ] = data_frame[ i ].fillna( method = 'ffill' )
                
            elif( op == 5 ):
                
                data_frame[ i ] = data_frame[ i ].fillna( float( input("Enter data to be filled at null places = ") ) )
            else:
                print( "Wrong Input. Try Again !")
                
    print()
    print()
                
    return data_frame
