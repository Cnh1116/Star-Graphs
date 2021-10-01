import matplotlib.pyplot as plt
import numpy as np


x = ()
y = ()
MaxLength = 20

#Star Graph------------------------------------------------------------
#for i in range(1,MaxLength):
    #Quad1XValues = [i, 0]
    #Quad1YValues = [0, (MaxLength-(i-1))]
   # Quad2XValues = [-i, 0]
   # Quad2YValues = [0, MaxLength-(i-1)]
   # Quad3XValues = [-i, 0]
   # Quad3YValues = [0, -MaxLength+(i-1)]
   # Quad4XValues = [i, 0]
   # Quad4YValues = [0, -MaxLength+(i-1)]

    #plt.plot(Quad1XValues, Quad1YValues, 'm')
    #plt.plot(Quad2XValues, Quad2YValues, 'm')
    #plt.plot(Quad3XValues, Quad3YValues, 'm')
    #plt.plot(Quad4XValues, Quad4YValues, 'm')

# #Origin Lines (Star Graph)
#plt.plot([-MaxLength+1, MaxLength-1],[0,0], 'm')
#plt.plot([0, 0],[-MaxLength, MaxLength], 'm')

#45 Rotated Star Graph--------------------------------------------------
for i in range(1,MaxLength+1):
    Quad1XValues = [i, MaxLength-(i-1)]
    Quad1YValues = [i, -MaxLength+(i-1)]
    Quad2XValues = [i, -MaxLength+(i-1)]
    Quad2YValues = [-i, -MaxLength+(i-1)]
    Quad3XValues = [-i, -MaxLength+(i-1)]
    Quad3YValues = [-i, MaxLength-(i-1)]
    Quad4XValues = [-i, MaxLength-(i-1)]
    Quad4YValues = [i, MaxLength-(i-1)]

    plt.plot(Quad1XValues, Quad1YValues, 'g')
    plt.plot(Quad2XValues, Quad2YValues, 'g')
    plt.plot(Quad3XValues, Quad3YValues, 'g')
    plt.plot(Quad4XValues, Quad4YValues, 'g')

#Origin Lines (45 Rotated Star Graph)
plt.plot([-MaxLength, MaxLength],[-MaxLength, MaxLength], 'g')
plt.plot([-MaxLength, MaxLength],[MaxLength, -MaxLength], 'g')

#----------------------------------------------------------------------------------------
# naming the x axis
plt.xlabel('x - Axis')
# naming the y axis
plt.ylabel('y - Axis')
 
# giving a title to my graph
plt.title('Rotated Star Graph!')
plt.grid(linewidth=2)
# function to show the plot
plt.show()