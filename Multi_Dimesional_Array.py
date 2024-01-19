import numpy as np;

# Multi dimensional array
z= np.array([[1,2,3,4],[5,6,7,8]]) # 2 dimensional
w= np.array([[1,2,3],[5,6,7],[4,5,6]]) #3 dimensional
print(z)
print(z.ndim) # find the dimension of array

p = np.array([1,2,3,4],ndmin=2) # give the dimension of the array
print(p)
#now p is a two dimesional array
