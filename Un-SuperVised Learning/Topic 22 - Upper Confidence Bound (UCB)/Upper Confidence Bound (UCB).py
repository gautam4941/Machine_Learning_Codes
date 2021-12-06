import pandas as pd
import random

data = pd.read_csv(r"C:\Users\gauta\PycharmProjects\MachineLearning\Un-SuperVised Learning\Topic 22 - Upper Confidence Bound (UCB)\Ads_CTR_Optimisation_with_choice2.csv")

"""
print( f"data.head() :- \n{ data.head() }\n" )
print( f"data.shape :- \n{ data.shape }\n" )

selected_columns = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
reward = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

total_reward = 0

arms = 10
for i in range( len( data.index ) ):    #0, 1, 2, ..., 9999
    col = random.randrange( arms )
    selected_columns[col] = selected_columns[col] + 1

    reward[col] = reward[col] + data.iloc[i, col]
    total_reward = total_reward + data.iloc[i, col]

print(f"total_reward = { total_reward }")
print(f"selected_columns = { selected_columns }")
print(f"reward = { reward }")

machine_names = [ 'Machine' ] * 10

for i in range( 1, 11 ):
    machine_names[ i - 1 ] = machine_names[ i - 1 ] + ' ' + str(i)

import matplotlib.pyplot as plt
plt.plot( machine_names , selected_columns)
plt.title( 'Histogram' )
plt.xlabel( 'Machines' )
plt.ylabel( 'No. of Times Each machine was selected' )
plt.show()

plt.plot( machine_names, reward )
plt.title( 'Histogram' )
plt.xlabel( 'No. of Times Each Ad was selected' )
plt.ylabel( 'Rewards' )
plt.show()
"""


data = pd.read_csv(r"C:\Users\gauta\PycharmProjects\MachineLearning\Un-SuperVised Learning\Topic 22 - Upper Confidence Bound (UCB)\Ads_CTR_Optimisation_with_choice2.csv")


#Understanding the approach only. This is not the main algorithm
selected_columns = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]      #n(i)
reward = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]                #r(i)
total_reward = 0
arms = 10

print( f"selected_columns = { selected_columns }")
print( f"reward = { reward }")
print( f"total_reward = { total_reward }")


import math

for i in range( len( data ) ):  # 10,000 times. person is going to pull the arm
    max_upper_bound = 0
    max_upper_bound_col = 0
    print(f"i = {i}")
    for j in range(1, 11):  # We have 10 machines, so he can select any random machine at a time
        reward_avg = 0
        if (selected_columns[j] > 0):
            print( "Inside IF" )
            reward[j] = reward[j] + data.iloc[ i, j ]

            reward_avg = reward[j] / selected_columns[j]  # User can select any machine at any round. So, we need
            # to find the average of reward. Later we will increment,
            # reward_sum for each selection and increment of no. of
            # selection also.\n",

            del_i = math.sqrt(3 / 2 * math.log(i) / selected_columns[j] )  # We will find the del_i for each selection in every round\n",
            upper_bound = reward_avg + del_i  # At last we are finding upper_bound for each round.\n",
        else:
            upper_bound = 1e400

        if (upper_bound > max_upper_bound):
            max_upper_bound = upper_bound
            max_upper_bound_col = j

        print(f"     j = {j}")
        print(f"     max_upper_bound = { max_upper_bound }" )
        print(f"     max_upper_bound_col = { max_upper_bound_col }" )
        print(f"     Inside, reward_avg = {reward_avg}")
        print(f"     Inside, selected_columns = {selected_columns}")
        print(f"     Inside, reward = {reward}")
        print(f"     upper_bound = {upper_bound}\n")

    selected_columns[max_upper_bound_col] = selected_columns[max_upper_bound_col] + 1

del selected_columns[0]
del reward[0]

print( f"selected_columns = { selected_columns }")
print( f"reward = { reward }")
print( f"total_reward = { total_reward }")


import matplotlib.pyplot as plt
plt.bar( range( 1, len(selected_columns)+ 1 ),  selected_columns  )
plt.title( 'Machine Selection Bar Graph.' )
plt.xlabel( "Machine Name -->" )
plt.ylabel( "No of Times Each Machine selected -->" )
plt.show()
