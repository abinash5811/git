import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr)
# print()
# print(sum(arr))
# print(np.mean(arr))

arr1=np.random.randint(0,40,size=10)
# arr_sort=np.sort(arr1)
# print(arr1)
# print()
# print(arr_sort)
# print()
# print(arr_sort**2)
# print()
# print(np.std(arr_sort))
arr_new=arr1.reshape(2,5)
arr_new1=np.arange(10)
print(arr_new)
print()
print(arr_new1)
print()
arr_new1.resize(2,5)
print(arr_new1)