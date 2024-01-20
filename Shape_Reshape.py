import numpy as np

# shape and reshape
#shape : output =(number of rows,number of columns)
arr = np.array([1,2,3,4],ndmin= 4)
print(arr)
print(arr.shape)

#reshape : change the dimension of the array, how to change the elements in an array
a1 = np.array([1,2,3,4,5,6,7,8,9])
new = a1.reshape(3,3)
print(new)
