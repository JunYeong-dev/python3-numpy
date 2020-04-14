import numpy as np

# 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

# 4 x 4의 2차원 배열을 만들고 초기값은 0, 데이터 타입은 float
array2 = np.zeros((4, 4), dtype=float)
print(array2)

# 4 x 4의 2차원 배열을 만들고 초기값은 1, 데이터 타입은 str
array3 = np.ones((4, 4), dtype=str)
print(array3)

# 0부터 9까지 랜덤하게 초기화 된 배열 만들기
array4 = np.random.randint(0, 10, (3, 3))
print(array4)

# 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0, 1, (3, 3))
print(array5)