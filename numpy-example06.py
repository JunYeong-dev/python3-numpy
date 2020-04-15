import numpy as np

# 균일한 간격으로 데이터 생성
# 0에서 10까지 중 균일한 간격으로 5개의 값을 생성
array1 = np.linspace(0, 10, 5)
print(array1)

# 난수의 재연 (실행마다 결과 동일)
np.random.seed(7)
print(np.random.randint(0, 10, (2, 3)))

# 배열 객체 복사
array2 = np.arange(0, 10)
# 밑의 결과 numpy의 경우 array2와 array3이 같은 주소를 가지게 됨
array3 = array2
# 따라서 array3의 0번째 값을 바꿨지만 array2의 값도 같이 변하게 됨
array3[0] = 99
print(array2)
# 그러므로 numpy에서 배열의 복사는 copy()함수를 사용
array4 = array2.copy()
# 서로 다른 주소 값을 가지므로 값을 바꿔도 서로 영향을 주지 않음
array4[1] = 77
print(array2)

# 중복된 원소 제거
array5 = np.array([1, 1, 5, 6, 7, 7, 7, 9])
print(np.unique(array5))