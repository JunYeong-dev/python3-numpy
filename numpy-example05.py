import numpy as np

# 원소 오름차순 정렬
array1 = np.array([9, 5, 2, 6, 3])
array1.sort()
print(array1)
# 원소 내림차순 정렬
# 인덱싱 기법을 이용하여 내림차순으로 정렬 가능
print(array1[::-1])

# 각 열을 기준으로 정렬
array2 = np.array([[5, 8, 2, 3, 7], [2, 4, 1, 8, 3]])
print(array2)
array2.sort(axis=0)
print(array2)