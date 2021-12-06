import pandas as pd

data = pd.read_csv(r"C:\Users\gauta\PycharmProjects\MachineLearning\Un-SuperVised Learning\Topic 23 - Thompson Sampling\Ads_CTR_Optimisation_with_choice2.csv")
print( data.head() )

"""
import random

machines = 10
selected_machines = []
count_selected_machines = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
reward = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
total_reward = 0

for i in range( len( data ) ):            #0, 1, 2, .., 9999
    col = random.randrange( machines )
    selected_machines.append( col )
    count_selected_machines[col] = count_selected_machines[col] + 1
    reward[col] = reward[col] + data.iloc[ i, col ]
    total_reward = total_reward + data.iloc[ i, col ]

print( f"selected_columns = { selected_machines }" )
print( f"total_reward = { total_reward }" )
print()
print( f"count_selected_columns = { count_selected_machines }" )
print( f"reward = { reward }" )

import matplotlib.pyplot as plt

plt.plot( count_selected_machines )
plt.title( 'Count Selected Machines' )
plt.xlabel( 'Machines ----> ' )
plt.ylabel( 'Selection Count  ---->' )
plt.show()

plt.plot( reward )
plt.title( 'Count Selected Machines' )
plt.xlabel( 'Machines ----> ' )
plt.ylabel( 'Selection Count  ---->' )
plt.show()
"""

#First we are going to analyze the UCB then, We will analyze the Thompson Sampling.
#Then, we can see the diffrence between both algorithms.

import random

reward_list_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
reward_list_0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
no_of_machine_selected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
machine_selected = []
total_reward = 0

print( f"reward_list_1 = { reward_list_1 }")
print( f"reward_list_0 = { reward_list_0 }")
print( f"no_of_machine_selected = { no_of_machine_selected }")
print( f"machine_selected = { machine_selected }")
print( f"total_reward = { total_reward }" )

for n in range( 10000 ):
    machine_no = 0
    max_random = 0
    for i in range(1, 11):
        random_beta = random.betavariate( reward_list_1[i] + 1, reward_list_0[i] + 1 )

        if( random_beta > max_random ):
            max_random = random_beta
            machine_no = i

    machine_selected.append( machine_no )
    no_of_machine_selected[ machine_no ] = no_of_machine_selected[ machine_no ] + 1

    reward = data.iloc[ n, machine_no ]

    if( reward == 0 ):
        reward_list_0[ machine_no ] = reward_list_0[ machine_no ] + 1
    else:
        reward_list_1[ machine_no ] = reward_list_1[ machine_no ] + 1

    total_reward = total_reward + reward

del reward_list_0[0]
del reward_list_1[0]
del no_of_machine_selected[0]

print()
print( f"machine_selected = { machine_selected }")
print( f"total_reward = { total_reward }" )
print( f"reward_list_1 = { reward_list_1 }")
print( f"reward_list_0 = { reward_list_0 }")
print( f"no_of_machine_selected = { no_of_machine_selected }")


sum = 0
for i in reward_list_0:
    sum = sum + i

print( f"Sum( reward_list_0 ) = { sum }" )

sum = 0
for i in reward_list_1:
    sum = sum + i

print(f"Sum( reward_list_1 ) = {sum}")


import matplotlib.pyplot as plt
plt.bar( range(1, 11), no_of_machine_selected, label = 'NO OF MACHINE SELECTED'  )
plt.title( 'Machine Selection Bar Graph.' )
plt.xlabel( "Machine Name -->" )
plt.ylabel( "No of Times Each Machine selected -->" )
plt.legend()
plt.show()