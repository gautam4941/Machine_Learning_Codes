#When we work with histogram then we need to have only one data which will be x-axis data
#and y will be the freq. occurance of each element in x-axis data

import matplotlib.pyplot as plt
import random
import pandas as pd



# Syntax for Random,
# random.randrange(start_value, End_value, incrementation)
# random.randrange( 20, 50, 3 ) -> 20, 23, 26, 29, ... , 48

roll_no = []
for i in range(1, 41):  # 1, 2, .., 39, 40
    roll_no.append( random.randrange(1, 11, 1) )
print(f"roll_no = {roll_no}\n")

"""
plt.hist( roll_no, label = 'Roll_no V/s Count - Graph 1')
plt.xlabel('roll_no')
plt.ylabel('Occurance Freq')
plt.title( 'Histogram Graph' )
plt.legend()
plt.show()


plt.hist( roll_no, rwidth=0.9, label = 'Roll_no V/s Count - Graph 2')
plt.xlabel('roll_no')
plt.ylabel('Occurance Freq')
plt.title( 'Histogram Graph' )
plt.legend()
plt.show()


#bin is about the no of categories belong to some to some range.
#Ex :- Out of 40. 15 data are belonging from 1 to 4 range
#Ex :- Out of 40. 12 data are belonging from 4 to 7 range
#Ex :- Out of 40. 13 data are belonging from 7 to 10 range
plt.hist( roll_no, rwidth=0.9, bins = 3, label = 'Roll_no V/s Count - Graph 2')
plt.xlabel('roll_no')
plt.ylabel('Occurance Freq')
plt.title( 'Histogram Graph' )
plt.legend()
plt.show()
"""


#If we want to give custom ranges

marks = []
for i in range( 1, 50 ):
    marks.append( random.randrange(1, 101, 10) )

print( f"marks = { marks }\n" )


# 1 to 35 -> Fail
# 36 to 60 -> Just Pass
# 61 to 70 -> Pass
# 71 to 80 -> Good
# 81 to 90 -> Very Good
# 91 to 100 -> Excellent

"""
plt.hist( marks, rwidth=0.9, bins = [ 1, 36, 61, 71, 81, 91, 101 ], label = 'Roll_no V/s Count - Graph 2')
plt.xlabel('Marks')
plt.ylabel('Occurance Freq')
plt.title( 'Histogram Graph - Marks Distribution' )
plt.legend()
plt.show()


plt.hist( marks
          , rwidth=0.9
          , bins = [ 1, 36, 61, 71, 81, 91, 101 ]
          , color = 'green'
          , histtype = 'step'
          , label = 'Roll_no V/s Count - Graph 2')
plt.xlabel('Marks')
plt.ylabel('Occurance Freq')
plt.title( 'Histogram Graph - Marks Distribution' )
plt.legend()
plt.show()
"""

"""
#plotting Multiple data at a time
class_A_marks = marks.copy()
class_B_marks = []
for i in range( 1, 50 ):
    class_B_marks.append( random.randrange(1, 101, 10) )

print( f"class_A_marks :- \n{ class_A_marks }\n" )
print( f"class_B_marks :- \n{ class_B_marks }\n" )

plt.hist( [ class_A_marks, class_B_marks ]
          , rwidth = 0.9
          , bins = [ 1, 36, 61, 71, 81, 91, 101 ]
          , color = [ 'red', 'green' ]
          , label = ['Class A', 'Class B'] )
plt.xlabel('Class A V/s Class B')
plt.ylabel('Occurance Freq')
plt.title( 'Histogram Graph - Marks Distribution' )
plt.legend()
plt.show()


plt.hist( [ class_A_marks, class_B_marks ]
          , rwidth = 0.9
          , bins = [ 1, 36, 61, 71, 81, 91, 101 ]
          , color = [ 'red', 'green' ]
          , label = ['Class A', 'Class B']
          , orientation = 'horizontal'
          )
plt.xlabel('Class A V/s Class B')
plt.ylabel('Occurance Freq')
plt.title( 'Histogram Graph - Marks Distribution' )
plt.legend()
plt.show()
"""


hr_data = pd.read_csv( r"C:\Users\gauta\PycharmProjects\MachineLearning\Pre Processing\Topic 3 - MatPlotLib\Data\hrdata.csv" )
'''
import pandas as pd


print( f"hr_data.head() :- \n{ hr_data.head() }\n" )
print( f"hr_data.columns = { hr_data.columns }\n" )

plt.hist( hr_data['Income'], bins = 10, color = 'red', alpha = 0.2, label = 'alpha = 0.2' )
plt.legend()
plt.show()

plt.hist( hr_data['Income'], bins = 10, color = 'red', alpha = 0.3, label = 'alpha = 0.3' )
plt.legend()
plt.show()

plt.hist( hr_data['Income'], bins = 10, color = 'red', alpha = 0.4, label = 'alpha = 0.4' )
plt.legend()
plt.show()

plt.hist( hr_data['Income'], bins = 10, color = 'red', alpha = 0.5, label = 'alpha = 0.5' )
plt.legend()
plt.show()

plt.hist( hr_data['Income'], bins = 10, color = 'red', alpha = 0.6, label = 'alpha = 0.6' )
plt.legend()
plt.show()

plt.hist( hr_data['Income'], bins = 10, color = 'red', alpha = 0.7, label = 'alpha = 0.7' )
plt.legend()
plt.show()

plt.hist( hr_data['Income'], bins = 10, color = 'red', alpha = 0.8, label = 'alpha = 0.8' )
plt.legend()
plt.show()

#alpha range is from 0 to 1
'''