def find_outlier( x ):

    #dict which will hold outlier details
    outliers_dict = {}
    indexes = x.index
    
    #change the variable data type to dataframe if it's not a dataframe
    if( isinstance( x, pd.DataFrame ) == False ):
        x = pd.DataFrame( x )

    #all columns names in x_cols
    x_cols = list( x.columns )
    
    #Main Loop for Outlier -> Running loop for all columns
    for col in x_cols:

       #Don't do anything if the curr_col is holding string data
        if( x[col].dtype == 'O' ):
            pass

        #Proceed only with numerical data type
        else:
            #making the skeleton for the column in the current iteration
            #Ex :-
            #outliers_dict['Age'] = {}
            #            'lo' : {}
            #            'uo' : {}
            #            }

            outliers_dict[col] = {
                'lo' : {}
                , 'uo' : {}
                }

            #Logic for finding the lower and upper outlier margin
            curr_col = x[col]
            describe = dict( curr_col.describe() )
            desc_25 = describe['25%']
            desc_75 = describe['75%']
            iqr = 1.5 * ( desc_75 - desc_25 )
            lower_outlier_margin = desc_25 - iqr
            upper_outlier_margin = desc_75 + iqr

	    # print( f"col = {col}, iqr = {iqr}, desc_25 = {desc_25}, lower_outlier_margin = {lower_outlier_margin}, desc_75 = {desc_75} and upper_outlier_margin = {upper_outlier_margin}\n\n" )
	    #Finding the outlier with index for column in current iteration

            for index in indexes:
                curr_data = curr_col[index]

                
                if( curr_data < lower_outlier_margin ):
                    outliers_dict[col]['lo'][index] = curr_data

                elif( curr_data > upper_outlier_margin ):
                    outliers_dict[col]['uo'][index] = curr_data

    return outliers_dict

def show_outlier_graph( data, outlier_col_vals ):
    #NOTE :- you should be sending dictionary data as 1st argument in following formate,
    #outlier_col_vals = {'col1': {'lo': { index1 : data1, .. }, 'uo': {index1 : data1, ..} }
            # , .. }
    
    #import matplotlib module
    import matplotlib.pyplot as plt

    #run loop for each column
    for col in outlier_col_vals:
        
        #check if any column has any lower and upper outlier data or not
        if( ( len( outlier_col_vals[col]['lo'] ) == 0 )
            and ( len( outlier_col_vals[col]['uo'] ) == 0 ) ):
            pass

        #show boxplot for the outlier columns from the dataset
        else:
            data[col].plot( kind = 'box' )
            plt.title( col )
            plt.show()
