def label_encoding( x ):
    print( f"Inside Label Encoding function ...\n" )
    print( f"Importing LabelEncoder..." )
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    print( f"Imported LabelEncoder...\n" )

    print( f"Going Inside Loop ...\n" )
    for i in list( x.columns ):
        if( x[i].dtype == object ):
            print( f"Encoding Column :- {i}" )
            print( f"Before Encoding, Unique Values :- \n{ x[i].value_counts() }\n")
            x[i] = le.fit_transform( x[i] )
            print( f"After Encoding, Unique Values :- \n{ x[i].value_counts() }\n\n")
