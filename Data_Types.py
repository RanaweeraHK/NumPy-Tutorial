import numpy as np

#Data types
y = np.array([1,2,3,4],dtype="U") # change the integers into string
z = np.array([1,2,3,4],dtype="f") # change the integers into floats

print(z.dtype) #check what is the data type

#string can't convert into integer or float
# s = np.array(["python","c++"],dtype="i") wrong

m= np.array([1.9,0,2.3,0,5])
n= m.astype("bool")  # array.astype(data type)
print(m)
print(m.dtype)
print(n)
print(n.dtype)
