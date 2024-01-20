import numpy as np

# Searching
arr = np.array([1,2,3,4,5,6])
print(np.where(arr==4)) # output the index and datatype
print(np.where(arr%2==0)) #output the indexes of all even numbers
