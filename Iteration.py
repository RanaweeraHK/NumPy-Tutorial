import numpy as np

#Iteration

#2 dimensional array
#method 1
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in x:
    for j in i:
        print(j)

#method 2
for i in np.nditer(x[:,:2]):  #np.nditer(array[start:end:step size])
    print(i)

#output both index and element
for i,j in np.ndenumerate(x):
    print(i,j)
