import numpy as np;

# Array indexing
s= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(s)
print(s[2,0]) #output=7 3rd row 1st column

m = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[11,12,13]]])
print(m)
print(m[1,0,2]) #output =9

n = np.array([1,2,3,4]) #negative indexing
print(n[1])
print(n[-3])
