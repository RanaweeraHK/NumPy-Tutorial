import numpy as np

# Array slicing
a= np.array([1,2,3,4,5]) #one dimesional array
print(a[1:4:2]) #a[start:end:step]

x= np.array([[1,2,3],[3,4,5],[6,7,8]])
print(x)
print(x[1,0:]) # 2nd column all elements
print(x[:,2]) # last element of each row
