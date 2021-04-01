import matplotlib.pyplot as plt

weight = [60, 79, 81, 65, 98, 67]
names = ['Ram', 'Shyam', 'Ritu', 'Soni', 'Rahul', 'Ranjan']
print( f"len(weight) = {len(weight)}" )
print( f"len(names) = {len(names)}" )

#plt.pie( [60, 79, 81, 65, 98, 67], ['Ram', 'Shyam', 'Ritu', 'Soni', 'Rahul', 'Ranjan'] )
plt.pie( weight, labels = names )
plt.title('Roll v/s Count')
plt.show()

plt.pie( weight, labels = names, startangle = 90 )    #Pie Chart will start displaying with 90 of Angle.
plt.title('Roll v/s Count')
plt.show()

plt.pie( weight, labels = names, startangle = 90, shadow = True )    #Shadow will give shadow like Texture.
plt.title('Roll v/s Count')
plt.show()

weight = [60, 79, 81, 65, 98, 67]
names = ['Ram', 'Shyam', 'Ritu', 'Soni', 'Rahul', 'Ranjan']

#Explode will make the peice of pie chart bit outside. We use it to attract the user attention to show
# important areas.
plt.pie( weight, labels = names, startangle = 90, shadow = True, explode = (0, 0, 0.1, 0, 0.1, 0) )
plt.title('Roll v/s Count')
plt.show()

#Explode will make the peice of pie chart bit outside. We use it to attract the user attention to show important areas.
plt.pie( weight, labels = names, startangle = 90, shadow = True, explode = (0, 0, 0.5, 0, 0.5, 0) )
plt.title('Roll v/s Count')
plt.show()

#Explode will make the peice of pie chart bit outside. We use it to attract the user attention to show important areas.
plt.pie( weight, labels = names, startangle = 90, shadow = True, explode = (0, 0, 1, 0, 1, 0) )
plt.title('Roll v/s Count')
plt.show()


#Explode will make the peice of pie chart bit outside. We use it to attract the user attention to show important areas.
plt.pie( weight, labels = names, startangle = 90, shadow = True, explode = (0, 1, 0.1, 0, 4, 0) )
plt.title('Roll v/s Count')
plt.show()

