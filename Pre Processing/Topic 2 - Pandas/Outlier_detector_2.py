def detect_outlier( data ):
    col_to_processed = []

    data_dtypes = dict( data.dtypes )
    for col, dtype in data_dtypes.items():
        # print( f"col = { col } and dtype = { dtype }" )

        if( data_dtypes[col] != 'O' ):
            col_to_processed.append( col )

    # print( f"col_to_processed = { col_to_processed }" )

    outlier_dict = {}

    for col in col_to_processed:
        outlier_dict[col] = {}
        
        describe = dict( data[col].describe() )

        iqr = 1.5 * ( describe['75%'] - describe['25%'] )
        lower_outlier = describe['25%'] - iqr
        upper_outlier = describe['75%'] + iqr

        outlier_dict[col]['lower_outlier'] = dict( data[col][ data[col] < lower_outlier ] )
        outlier_dict[col]['upper_outlier'] = dict( data[col][ data[col] > upper_outlier ] )

        # print( f"For {col}, lower_outlier_df :- \n{ lower_outlier_df }\n" )
        # print( f"For {col}, type( lower_outlier_df ) :- \n{ type( lower_outlier_df ) }\n" )

    for col, details in outlier_dict.items():
        print( f"{col} :- \n{ outlier_dict[col] }\n" )
