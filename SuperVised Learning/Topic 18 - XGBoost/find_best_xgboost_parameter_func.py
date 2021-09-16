def find_best_xgboost_parameter( x, y ):
    max_acc = 0

    good_subsample = 0
    good_n_estimators = 0
    good_learning_rate = 0
    
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2, random_state = 0 )

    from xgboost import XGBRFClassifier

    # subsample Loop -> 10 times
    p_subsample = 0
    for i in range( 1, 11 ):
        p_subsample = p_subsample + 0.1

        p_n_estimators = 0
        # n_estimators Loop -> 10 times
        for j in range( 1, 11 ):
            p_n_estimators = p_n_estimators + 50

            p_learning_rate = 0
            # learning_rate Loop -> 10 times
            for k in range( 1, 11 ):
                p_learning_rate = p_learning_rate + 0.1

                print( f"p_subsample = { p_subsample }, p_n_estimators = { p_n_estimators }, p_learning_rate = { p_learning_rate }", end = ' and ' )
                
                xgboost = XGBRFClassifier( max_depth = 100
                                    , subsample = p_subsample
                                    , n_estimators = p_n_estimators
                                    ,learning_rate = p_learning_rate )

                xgboost.fit( x_train, y_train )
                y_pred = xgboost.predict( x_test )

                acc = xgboost.score( x_test, y_test )
                print( f"acc = { acc }" )
                
                if( acc > max_acc ):
                    max_acc = acc
                    good_subsample = p_subsample
                    good_n_estimators = p_n_estimators
                    good_learning_rate = p_learning_rate

    return max_acc, good_subsample, good_n_estimators, good_learning_rate
