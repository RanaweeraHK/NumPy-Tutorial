import numpy as np

a= np.array([1,2,3,4])
b= a.copy()
c= a.view()

a[0] =9
print(a) #changed
print(b) #not changed
print(c) #changed

print(a.base)  #check the original data of these arrays
print(b.base)
print(c.base)
