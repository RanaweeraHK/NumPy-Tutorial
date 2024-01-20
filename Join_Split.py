import numpy as np

#join and split
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
newArr = np.concatenate((arr1,arr2),axis =0) #default axis=0
print(newArr)

arr3 = np.array([[1,2,3],[4,5,6]])
arr4 = np.array([[7,8,9],[10,11,12]])
newArr = np.concatenate((arr3,arr4),axis=1)
print(newArr)

newArr = np.array_split(arr3,2) #np.array_split(array name, number of sections)
print(newArr)
