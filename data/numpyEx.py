import numpy as np

arr1 = np.arange(15).reshape(3,5)

print(arr1)
print(arr1.shape)

arr2 = np.zeros((3,5))
print(arr2)

arr3 = np.ones((3,5))
arr3 = arr3 * 5

print(arr1 + arr3)
print(arr1 - arr3)
print(arr1 * arr3)
print(arr1 / arr3)