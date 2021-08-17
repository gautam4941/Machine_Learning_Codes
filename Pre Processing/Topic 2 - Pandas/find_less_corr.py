def find_less_corr( x_data, y_data ):
    if( isinstance( y_data, pd.DataFrame ) == False ):
        y_data = pd.DataFrame( y_data )
       
    y_col = list( y_data.columns )[0]
    x['y'] = y_data
    
    corr_data = dict( x.corr()['y'] )
    
    less_corr_cols = {}
    for col, corr in corr_data.items():
        if( corr < 0 ):
            corr = corr * -1
            
        if( corr < 0.1 ):
            # print( f"{col} : {corr}" )
            less_corr_cols[col] = corr
            
    while( True ):
        graph_op = input("Do you want to see 1. Graphs for all the low corr columns, 2. No = " )
        if( graph_op.isdigit() ):
            graph_op = int( graph_op )
            break
            
        else:
            print( "Enter correct Integer Option" )
            
    
    if( graph_op == 1 ):        
        import matplotlib.pyplot as plt
        
        for col, corr in less_corr_cols.items():
            plt.plot( x[col], linestyle = '', marker = '*' )
            plt.title( f"{col} : {corr}" )
            plt.xlabel(col)
            plt.show()
        
    return less_corr_cols