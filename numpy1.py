# 이번 시간에는 넘파이 기초를 실습을 해볼 예정이다.

# 배열 생성

data1 = [1, 2, 3, 4, 5]
a1 = np.array(data1)
a1

data1에 위와 같이 정수 1차원 배열을 정의했고, numpy 배열로 재정의한 a1은 array([1, 2, 3, 4, 5])을 출력한다. 

data2 = [0.1, 5, 4, 12, 0.5]
a2 = np.array(data2)
a2

data2 배열을 numpy 배열로 바꾸면 array([ 0.1,  5. ,  4. , 12. ,  0.5])을 출력한다. 여기서 5, 4, 12 정수는 실수타입으로 바뀌면서 .이 붙게된다.

a1.dtype

위 a1의 타입을 묻는데 정수만 존재하므로 dtype('int64')을 출력한다.

a2.dtype

위 a2의 타입을 묻는데 실수가 존재하므로 dtype('float64')을 출력한다.

np.array([[1,2,3], [4,5,6], [7,8,9]])

2차원 행렬을 정렬하면 
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]) 을 출력한다.

np.arange(0, 10, 2) 

range함수와 동일하고 0~9까지 2스텝씩 더하여 배열을 생성하면 array([0, 2, 4, 6, 8])를 출력한다.

np.arange(1, 11)

1~10까지 1씩 더하여 array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])를 출력한다.

np.arange(5)

0~4까지 1씩 더하여 array([1, 2, 3, 4])를 출력한다.

np.arange(12).reshape(4,3)

reshape함수는 0~11를 4x3 행렬로 바꿔준다. 따라서
array([[ 0,  1,  2],
       [ 3,  4,  5],
       [ 6,  7,  8],
       [ 9, 10, 11]])를 출력한다.

b1 = np.arange(12).reshape(4,3)
b1.shape

b1은 위의 array와 같은데 그 shape을 묻는것이므로 (4, 3)를 출력한다.

b2 = np.arange(5)
b2.shape

array([0, 1, 2, 3])의 shape을 묻는것이므로 (5,)를 출력한다. ,를 찍지 않으면 (5)는 정수로 인식하므로 조심해야한다.

np.linspace(1, 10, 10)

1부터 10까지를 10개로 균등하게 나누라는 뜻이므로 array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.])를 출력한다.

np.linspace(0, np.pi, 20 )

0부터 np.pi(3.14)까지 20개로 균등하게 나누라는 뜻이므로 
array([0.        , 0.16534698, 0.33069396, 0.49604095, 0.66138793,
       0.82673491, 0.99208189, 1.15742887, 1.32277585, 1.48812284,
       1.65346982, 1.8188168 , 1.98416378, 2.14951076, 2.31485774,
       2.48020473, 2.64555171, 2.81089869, 2.97624567, 3.14159265])를 출력한다.
linspace는 그래프 곡선을 그릴떄 부드럽게 그리기 위해 많이 사용되므로 기억하자.

np.zeros(10)

0을 10개로 채우라는 뜻이므로 array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])를 출력한다.

np.zeros((3,4))

0을 3x4배열로 채우라는 뜻이므로
array([[0., 0., 0., 0.], 
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])를 출력한다.

np.ones(5)

1을 5개로 채우라는 뜻이므로 array([1., 1., 1., 1., 1.])를 출력한다.

np.ones((3,5))

1을 3x5배열로 채우라는 뜻이므로
array([[1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1.]])를 출력한다.

np.eye(10, k=-1)

array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.]])
대각행렬인데 k=0일때 가장 가운데 대각선을 1로 채우게 되고 그 1로 이루어진 선은 k가 양수면 위로, k가 음수면 아래로 이동한다.

np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
a = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
a.dtype

''를 보아하니 문자열로 구성된 array이므로 Unicode를 출력하는데 문자열중 가장 개수가 많은 3.141592의 8개를 붙여서 U8, 즉 dtype('<U8')로 출력한다.
숫자 아니다. 헷갈리면 안된다.

str_a1 = np.array(['1.567', '0.123', '5.123', '9', '8'])
num_a1 = str_a1.astype(float)
print(num_a1)
print(type(num_a1))

String함수를 float함수로 형변환 시켜주면 다음과 같다. [1.567 0.123 5.123 9.    8.   ] 그리고 이것의 type은 <class 'numpy.ndarray'>이다.

str_a1.dtype

위의 array는 문자열이므로 Unicode이고, 가장 많은 개수의 문자열이 5개이므로 U5, 즉 dtype('<U5')이다.

num_a1.dtype

num의 경우 default가 float64이므로 dtype('float64')이다.

str_a2 = np.array(['1', '3', '5', '7', '9'])
num_a2 = str_a2.astype(int)
num_a2

str를 int로 형변환하면 문자열을 정수로 바꿔준다. array([1, 3, 5, 7, 9])

str_a2.dtype

문자열 a2의 type은 U1, dtype('<U1')

num_a2.dtype

num은 정수 default인 int64, dtype('int64')

num_f1 = np.array([10, 21, 0.549, 4.75, 5.98])
num_i1 = num_f1.astype(int)
num_i1

float를 int로 변환시키면 array([10, 21,  0,  4,  5])

num_f1.dtype

float의 default는 float64, dtype('float64')

num_i1.dtype 

int의 default는 int64, dtype('int64')

np.random.rand(2,3)

위 rand함수는 난수로 생성된 2x3행렬을 만든다.
array([[0.92190333, 0.72498335, 0.64158492],
       [0.18969004, 0.6962214 , 0.26577442]])

np.random.rand()

위 rand함수는 난수 1개를 만든다.
0.6951250487078596

np.random.rand(2,3,4)
a = np.random.rand(2,3,4)
print(a)

위 rand함수는 난수로 생성된 2x3x4행렬(3x4행렬 2개)을 만든다.
[[[0.24724296 0.27443511 0.9675693  0.72599926]
  [0.06275644 0.14079102 0.25860388 0.26298507]
  [0.21402957 0.46580311 0.02200673 0.82944533]]

 [[0.92622922 0.39890741 0.10642596 0.12637467]
  [0.46498714 0.78962067 0.37460483 0.15467044]
  [0.16724974 0.25927002 0.86215493 0.80990086]]]

np.random.randint(10, size=(3, 4))

위 rand함수는 정수로 10까지의 난수를 3x4행렬로 만든다.
array([[1, 4, 3, 5],
       [6, 7, 5, 9],
       [1, 1, 0, 0]])

np.random.randint(1, 30)

위 rand함수는 정수로 1~30까지의 난수를 1개 만든다.
18

# 배열 연산

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

arr1 + arr2

둘을 더하면 array([11, 22, 33, 44])

arr1 - arr2

둘을 빼면 array([ 9, 18, 27, 36])

arr2 * 2 

arr2에 2를 곱하면 array([2, 4, 6, 8])

arr1 / (arr2 ** 2)

arr1을 arr2의 제곱으로 나누면 array([10.        ,  5.        ,  3.33333333,  2.5       ])

arr1 > 20

arr1이 20보다 큰가?에 대한 질문에는 각각 대조하여 array([False, False,  True,  True])

# 통계 연산

arr3 = np.arange(5)
arr3

arr3은 0~4까지 배열하는것이므로 array([0, 1, 2, 3, 4])

[arr3.sum(), arr3.mean()]

sum: 총합, mean: 평균 을 각각 의미하므로 [10, 2.0]

[arr3.std(), arr3.var()]

std: 표준편차(분산을 제곱근), var: 분산(평균과의 편차 제곱 후 더한다음 나누기 개수)를 의미하므로 [1.4142135623730951, 2.0]

[arr3.min(), arr3.max()]

arr3 배열의 최소와 최대를 의미하므로 [0, 4]

arr4 = np.arange(1,5)
arr4

arr4를 1~4까지 배열로 정의하므로 array([1, 2, 3, 4])

arr4.cumsum()

cumsum: cumulative sum(누적합)을 의미하므로 array([ 1,  3,  6, 10])

arr4.cumprod()

cumprod: 누적곱을 의미하므로 array([ 1,  2,  6, 24])

# 행렬 연산

A = np.array([0, 1, 2, 3]).reshape(2,2)
A

array A를 2x2 배열로 바꾸는것이므로 
array([[0, 1],
       [2, 3]])

B = np.array([3, 2, 0, 1]).reshape(2,2)

array B를 2x2 배열로 바꾸는것이므로 
array([[3, 2],
       [0, 1]])

A.dot(B)              

dot은 행렬곱하기이므로 
0, 1      3 | 2
----   X    |
2, 3      0 | 1  

array([[(0*3)+(1*0), (0*2)+(1*1)],
       [(2*3)+(3*0), (2*2)+(3*1)]])
즉,
array([[0, 1],
       [6, 7]])

np.dot(A,B)

위와 같은 질문이다.
array([[0, 1],
       [6, 7]])

np.transpose(A)

transpose는 전치행렬이므로 가로 세로 한번씩 뒤집어준다 
array([[0, 2],
       [1, 3]])

A.transpose()

위와 같은 질문이므로,
array([[0, 2],
       [1, 3]])

data:image/png;base64,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

np.linalg.det(A)

역행렬이므로 대각으로 서로 곱한다. -2.0

np.linalg.inv(A)

역행렬 식을 이용해서      (3 -1)
                     1/2(2  0)
array([[-1.5,  0.5],
       [ 1. ,  0. ]])


# 배열의 인덱싱

a1 = np.array([0, 10, 20, 30, 40, 50])
a1

array([ 0, 10, 20, 30, 40, 50])

a1[0]

a1의 0번째 열은 0이다. (0,1,2,3,~~)

a1[4] 

a1의 4번째 열은 40이다. (0,1,2,3,~~~)

a1[5] = 70
a1

a1의 5번째에 70을 추가하므로 a1은
array([ 0, 10, 20, 30, 40, 70])

a2 = np.arange(10, 100, 10).reshape(3,3)
a2

10~100까지 10 간격으로 3x3배열로 바꾸면
array([[10, 20, 30],
       [40, 50, 60],
       [70, 80, 90]])

a2[0, 2]

a2의 0행 2열은 30이다. (그냥 좌표를 묻는것)
30

a2[2, 2] = 95
a2

a2의 2행 2열을 95로 바꾸면
array([[10, 20, 30],
       [40, 50, 60],
       [70, 80, 95]])

a2[1]

a2의 1행을 뽑으면
array([40, 50, 60])

a2[1] = np.array([45, 55, 65])
a2

a2의 1행을 위와 같이 바꾸면
array([[10, 20, 30],
       [45, 55, 65],
       [70, 80, 95]])

a2[1] = [47, 57, 67]
a2

a2의 1행을 위와 같이 바꾸면 
array([[10, 20, 30],
       [47, 57, 67],
       [70, 80, 95]])

print(a2[[0, 2], [0, 1]])
a2[[0, 2], [0, 1]]

위의 인덱싱은 좀 다른데, 0행0열, 2행1열을 뽑으면
[10 80]

a = np.array([1, 2, 3, 4, 5, 6])
a[a > 3]

a 배열에서 3보다 큰 배열을 뽑으면
array([4, 5, 6])

a[(a % 2) == 0]

a 배열에서 짝수를 뽑으면
array([2, 4, 6])

b1 = np.array([0, 10, 20, 30, 40, 50])
b1[1:4]

b1 배열에서 1~3까지 뽑으면 
array([10, 20, 30])

b1[:3]

b1 배열에서 0~2까지 뽑으면
array([ 0, 10, 20])

b1[2:]

b1 배열에서 2부터 끝까지 뽑으면
array([20, 30, 40, 50])

b1[2:5] = np.array([25, 35, 45])
b1

b1 배열에 2~4까지 위와같이 바꾸면
array([ 0, 10, 25, 35, 45, 50])

b1[3:6] = 60
b1

b1 배열에서 3~5까지 위와같이 바꾸면
array([ 0, 10, 25, 60, 60, 60])

b2 = np.arange(10, 100, 10).reshape(3,3)
b2

b2 배열에서 10부터 100까지 10간격으로 3x3배열을 생성하면
array([[10, 20, 30],
       [40, 50, 60],
       [70, 80, 90]])

b2[1:3, 1:3]

b2 배열에서 1행1열, 2행2열을 인덱싱하면
array([[50, 60],
       [80, 90]])

b2[:3, 1:]

b2 배열에서 0행1열,2행0열. 1행1열,2행1열. 2행1열,2행2열을 인덱싱하면
array([[20, 30],
       [50, 60],
       [80, 90]])

b2[1][0:2]

b2 배열의 1행 전체에서 0~1열은 40, 50이므로
array([40, 50])

b2[0:2, 1:3] = np.array([[25, 35], [55, 65]])
b2

b2 배열의 0행1열,0행2열,1행1열,1행2열을 위와같이 바꾸면
array([[10, 25, 35],
       [40, 55, 65],
       [70, 80, 90]])




