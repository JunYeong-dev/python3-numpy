import numpy as np

# 배열 합치기(가로 축)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.concatenate([array1, array2])
print(array1)
print(array2)
print(array3)

# 배열의 형태 바꾸기 1차원 배열 -> 2차원 배열
array4 = np.array([1, 2, 3, 4])
array5 = array4.reshape((2, 2))
print(array4)
print(array5)

# 배열 합치기(세로 축)
array6 = np.arange(4).reshape(1, 4)
array7 = np.arange(8).reshape(2, 4)
array8 = np.concatenate([array6, array7], axis=0)
print(array6)
print(array7)
print(array8)

# 배열 나누기 세로 축
array9 = np.arange(8).reshape(2, 4)
left1, right1 = np.split(array9, [2], axis=1)
print(array9)
print(left1.shape)
print(right1.shape)
print(left1)
print(right1)

# 배열 나누기 가로 축
array10 = np.arange(8).reshape(2, 4)
left2, right2 = np.split(array10, [1], axis=0)
print(array10)
print(left2.shape)
print(right2.shape)
print(left2)
print(right2)