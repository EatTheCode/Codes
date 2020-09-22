import cv2 as cv
import numpy as np

#2x2 행렬 정의
mat0 = np.uint8([[130, 140], [150, 160]])
mat1 = np.uint8([[100, 100], [100, 100]])
mat2 = np.uint8([[145, 145], [145, 145]])

print('mat0'); print(mat0)
print('mat1'); print(mat1)
print('mat2'); print(mat2)

print('mat0 + mat1')
print(mat0 + mat1)
# 255만큼 표현 될수 있는데 그이상이 연산되어 오버플로우 발생 따라서 오버된 횟수 만큼이 표기됨

print('cv.add(mat0, mat1)')
print(cv.add(mat0, mat1))
# 이미지 두개를 더하는걸로 인식한는 연산
# 결과적으로 오버플로우가 발생하지 않음(표현가능한 수중 가장 가까운 수로 표현)


# 뺄셈 연산

print('mat0 - mat1')
print(mat0 - mat2)
# 초과된 횟수만큼 언더플로우 발생

print('cv.subtract(mat0, mat2)')
print(cv.subtract(mat0, mat2))
# 언더플로우되지않고 가까운 값을 표시


print('cv.addWeighted(mat0, 0.7, mat1, 0.3, 0)')
# mat0*0.7 + mat1*0.3 + gamma
print(cv.addWeighted(mat0, 0.7, mat1, 0.3, 0))
