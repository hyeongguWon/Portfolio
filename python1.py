# Q1. 홍길동의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수는?  
k = 80
e = 75
m = 55
average = (k+e+m) / 3
print('홍길동 씨의 평균 점수 : ' + str(average) + '입니다')

# Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법은?
num = 13
a = num % 2 # 2로 나눈 결과

if a == 0:
    print('짝수')
elif a == 1:
    print('홀수')

# Q3. 홍길동의 주민등록번호는 881120-1068234이다. 홍길동의 주민등록번호를 연월일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해보자
num = '881120-1068234'
YYYYMMDD = num[:6]
back = num[7:]
print(YYYYMMDD,back)

# Q4. 주민등록번호 뒷자리(Q3의 주민등록번호 사용)의 맨 첫번째 숫자는 성별을 나타낸다. 성별을 나타내는 숫자를 Q3과 연계해서 출력해보자
print(num[7])

# Q5. 다음과 같은 문자열 a:b:c:d:가 있다. 문자열의 replace 함수를 이용하여 a#b#c#d로 바꿔보자.
s = 'a:b:c:d'
new_s = s.replace(':','#') 
print(new_s)

# Q6. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1]로 만들어 보자. (Hint: sort()함수와 reverse()함수)
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

# Q7. ['Life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자. (Hint: join()함수)
a = ['Life', 'is', 'too', 'short']
new_a = ' '.join(a)
print(new_a)

# Q8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어 출력해 보자
a = (1,2,3) 
b = (4,) # (4)로 하게되면 type이 integer로 해석되므로, 4 끝에 ,를 붙여준다
c = a + b
print(c)

# Q9. 다음과 같은 딕셔너리 a가 있다. 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자.
    # 1. a['name'] = 'python'
    # 2. a[('a',)] = 'python'
    # 3. a[[1]] = 'python'
    # 4. a[250] = 'python'
1번은 키:밸류, 2번은 ('a',)가 키가 되어서 키:밸류 형태로, 4번은 250이 키가 되지만 3번은 대괄호가 두번 들어가는데 이는 존재하지 않는 문법이다. 각각 print(a)를 해서 비교해보자

# Q10. 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(result)

# Q11. a 리스트에서 중복 숫자를 제거해 보자 
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set_a = set(a)
print(set_a, type(set_a))
list_a = list(set_a)
print(list_a, type(list_a))

# Q12. 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 다음과 같이 a,b 변수를 선언한 후 a의 두 번째 요소값을 변경하면 b값은 어떻게 될까?
#       그리고 이런 결과가 나오는 이유에 대해 설명해보자
#   a = b = [1, 2, 3]
#   a[1] = 4
#   print(b)
#   => [1, 4, 3]

print(id(a))
print(id(b))
를 출력해보면 이론상으로는 말이 안되보이지만 실제 메모리에서는 같은 주소를 공유한다.
즉 a와 b는 같은 공간을 공유하므로, a를 바꾸면 b도 같이 바뀐다.
