import numpy as np

# 단일 객체 저장 및 불러오기
array1 = np.arange(0, 10)
# np.save(파일명, 저장할 객체)
np.save('saved.npy', array1)

result = np.load('saved.npy')
print(result)

# 복수 객체 저장 및 불러오기
array2 = np.arange(0, 10)
array3 = np.arange(10, 20)
# np.savez(파일명, 저장할 객체(각각의 객체 이름을 설정))
np.savez('saved.npz', array2=array2, array3=array3)

data = np.load('saved.npz')
result2 = data['array2']
result3 = data['array3']
print(result2)
print(result3)
